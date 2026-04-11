from flask import Flask, request, jsonify
from blog import Blog
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


def error_response(message, status_code=400):
    return jsonify({'error': message}), status_code


def success_response(data, status_code=200):
    return jsonify(data), status_code

@app.route('/blogs', methods=['POST'])
def create_blog():
    try:
        data = request.get_json()
        
        if not data or 'title' not in data or 'content' not in data:
            return error_response('Title and content are required')
        
        # Create Blog object and save to database
        blog = Blog(title=data['title'], content=data['content'])
        
        if blog.save():
            return success_response(blog.to_dict(), 201)
        else:
            return error_response('Failed to create blog', 500)
            
    except Exception as e:
        return error_response(f'Server error: {str(e)}', 500)

@app.route('/blogs', methods=['GET'])
def get_all_blogs():
    try:
        
        blogs = Blog.get_all()
        
        
        blogs_json = list(map(lambda b: b.to_dict(), blogs))
        
        
        published_blogs = list(filter(lambda b: b['content'] is not None, blogs_json))
        
        return success_response({
            'blogs': published_blogs,
            'count': len(published_blogs)
        })
        
    except Exception as e:
        return error_response(f'Server error: {str(e)}', 500)


@app.route('/blogs/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    try:
        
        blog = Blog.get_by_id(blog_id)
        
        if not blog:
            return error_response('Blog not found', 404)
        
        return success_response(blog.to_dict())
        
    except Exception as e:
        return error_response(f'Server error: {str(e)}', 500)


@app.route('/blogs/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    try:
      
        blog = Blog.get_by_id(blog_id)
        
        if not blog:
            return error_response('Blog not found', 404)
        
        data = request.get_json()
        
        if not data:
            return error_response('No data provided')
        
        title = data.get('title', blog.title)
        content = data.get('content', blog.content)
        
        if blog.update(title=title, content=content):
            return success_response(blog.to_dict())
        else:
            return error_response('Failed to update blog', 500)
            
    except Exception as e:
        return error_response(f'Server error: {str(e)}', 500)


@app.route('/blogs/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    try:
       
        blog = Blog.get_by_id(blog_id)
        
        if not blog:
            return error_response('Blog not found', 404)
        
       
        if blog.delete():
            return success_response({'message': 'Blog deleted successfully'})
        else:
            return error_response('Failed to delete blog', 500)
            
    except Exception as e:
        return error_response(f'Server error: {str(e)}', 500)


@app.route('/blogs/<int:blog_id>/translate', methods=['GET'])
def translate_blog(blog_id):
    try:
        
        blog = Blog.get_by_id(blog_id)
        
        if not blog:
            return error_response('Blog not found', 404)
        
        
        source_lang = request.args.get('source', 'auto')
        target_lang = request.args.get('target', 'en')
        
        
        result = blog.translate_and_speak(source_lang, target_lang)
        
        if not result:
            return error_response('Translation failed', 500)
        
        return success_response({
            'id': blog.id,
            'original_title': blog.title,
            'original_content': blog.content,
            'translated_content': result['translated_content'],
            'audio_file': result['audio_file']
        })
        
    except Exception as e:
        return error_response(f'Server error: {str(e)}', 500)


@app.route('/blogs/search', methods=['GET'])
def search_blogs():
    try:
        keyword = request.args.get('q', '')
        
        if not keyword:
            return error_response('Search query is required')
        
       
        blogs = Blog.search_blogs(keyword)
        
       
        result_blogs = []
        for blog in blogs:
            result_blogs.append(blog.to_dict())
        
        return success_response({
            'blogs': result_blogs,
            'count': len(result_blogs),
            'search_term': keyword
        })
        
    except Exception as e:
        return error_response(f'Server error: {str(e)}', 500)


@app.route('/health', methods=['GET'])
def health_check():
    return success_response({'status': 'healthy', 'message': 'Blog API is running'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)