import os
import subprocess
import platform
from datetime import datetime
from translate import Translator
from gtts import gTTS
from db import Database

class Blog:
    def __init__(self, id=None, title=None, content=None, created_at=None, updated_at=None):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = created_at
        self.updated_at = updated_at
        self.db = Database()
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': str(self.created_at) if self.created_at else None,
            'updated_at': str(self.updated_at) if self.updated_at else None
        }
    
    def save(self): 
        try:
            with self.db.get_cursor() as cursor:
                if self.id is None:
                    cursor.execute("""
                        INSERT INTO blogs (title, content) 
                        VALUES (%s, %s) 
                        RETURNING id, created_at, updated_at
                    """, (self.title, self.content))
                    
                    result = cursor.fetchone()
                    self.id = result[0]
                    self.created_at = result[1]
                    self.updated_at = result[2]
                else:
                    cursor.execute("""
                        UPDATE blogs 
                        SET title = %s, content = %s, updated_at = NOW() 
                        WHERE id = %s 
                        RETURNING updated_at
                    """, (self.title, self.content, self.id))
                    
                    result = cursor.fetchone()
                    self.updated_at = result[0]
                
                self.db.connection.commit()
                return True
        except Exception as e:
            print(f"Error saving blog: {e}")
            return False
    
    def update(self, title=None, content=None):
        try:
            if title:
                self.title = title
            if content:
                self.content = content
            
            return self.save()
        except Exception as e:
            print(f"Error updating blog: {e}")
            return False
    
    def delete(self):
        try:
            with self.db.get_cursor() as cursor:
                cursor.execute("DELETE FROM blogs WHERE id = %s", (self.id,))
                self.db.connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error deleting blog: {e}")
            return False
    
    def translate_and_speak(self, source_lang='auto', target_lang='en'):
        try:
           
            translator = Translator(from_lang=source_lang, to_lang=target_lang)
            translated_content = translator.translate(self.content)
            
            
            audio_dir = "audio"
            if not os.path.exists(audio_dir):
                os.makedirs(audio_dir)
            
            
            audio_file = f"{audio_dir}/blog_{self.id}_audio.mp3"
            tts = gTTS(text=translated_content, lang=target_lang, slow=False)
            tts.save(audio_file)
            
            
            self._play_audio(audio_file)
            
            return {
                'original_content': self.content,
                'translated_content': translated_content,
                'audio_file': audio_file
            }
        except Exception as e:
            print(f"Error in translate_and_speak: {e}")
            return None
    
    def _play_audio(self, audio_file):
        try:
            system = platform.system().lower()
            
            if system == 'darwin':  # macOS
                subprocess.run(['afplay', audio_file])
            elif system == 'linux':
                subprocess.run(['mpg123', audio_file])
            elif system == 'windows':
                subprocess.run(['start', audio_file], shell=True)
            else:
                print(f"Audio playback not supported on {system}")
        except Exception as e:
            print(f"Error playing audio: {e}")
    
    @staticmethod
    def get_all():
        try:
            db = Database()
            with db.get_cursor() as cursor:
                cursor.execute("SELECT id, title, content, created_at, updated_at FROM blogs ORDER BY created_at DESC")
                blogs_data = cursor.fetchall()
                
                
                blogs = list(map(lambda row: Blog(*row), blogs_data))
                return blogs
        except Exception as e:
            print(f"Error fetching all blogs: {e}")
            return []
    
    @staticmethod
    def get_by_id(blog_id):
        try:
            db = Database()
            with db.get_cursor() as cursor:
                cursor.execute("SELECT id, title, content, created_at, updated_at FROM blogs WHERE id = %s", (blog_id,))
                result = cursor.fetchone()
                
                if result:
                    return Blog(*result)
                return None
        except Exception as e:
            print(f"Error fetching blog by ID: {e}")
            return None
    
    @staticmethod
    def search_blogs(keyword):
        try:
            db = Database()
            with db.get_cursor() as cursor:
                cursor.execute("""
                    SELECT id, title, content, created_at, updated_at 
                    FROM blogs 
                    WHERE title ILIKE %s OR content ILIKE %s 
                    ORDER BY created_at DESC
                """, (f'%{keyword}%', f'%{keyword}%'))
                
                blogs_data = cursor.fetchall()
                
               
                blogs = list(map(lambda row: Blog(*row), blogs_data))
                
              
                filtered_blogs = list(filter(lambda blog: len(blog.content) > 0, blogs))
                return filtered_blogs
        except Exception as e:
            print(f"Error searching blogs: {e}")
            return []
        
    @staticmethod
    def delete_by_id(blog_id):
        try:
            db = Database()
            with db.get_cursor() as cursor:
                cursor.execute("DELETE FROM blogs WHERE id = %s", (blog_id,))
                db.connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error deleting blog by ID: {e}")
            return False
        
  