# Vamsi's Portfolio

A modern, responsive portfolio website built with Flask featuring a beautiful dark theme.

## Features

- 🎨 Modern dark theme with gradient accents
- 📱 Fully responsive design
- ⚡ Smooth animations and transitions
- 🚀 Fast and lightweight
- 📧 Contact form functionality
- 🎯 Project showcase section
- 📝 Easy to customize

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

## Customization

### Personal Information
Edit the following files to customize your portfolio:

1. **Update personal info in `app.py`:**
   - Modify the `projects` list with your actual projects
   - Update project descriptions, technologies, and links

2. **Customize the landing page in `templates/index.html`:**
   - Change the hero section text
   - Update the about section
   - Modify contact information

### Styling
The dark theme is defined in `templates/base.html`. You can customize:
- Colors and gradients
- Fonts and typography
- Animations and transitions
- Layout and spacing

### Adding New Projects
To add a new project, add an entry to the `projects` list in `app.py`:

```python
{
    'id': 5,
    'title': 'Your Project Title',
    'description': 'Brief description of your project',
    'technologies': ['Python', 'Flask', 'Other Tech'],
    'github_url': 'https://github.com/yourusername/project',
    'live_url': 'https://your-project-url.com',
    'image': 'project-image.jpg'
}
```

## Project Structure

```
portfolio/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── templates/
    ├── base.html      # Base template with styling
    └── index.html     # Main landing page
```

## Deployment

### Local Development
The app runs on `http://localhost:5000` by default.

### Production Deployment
For production deployment, consider:
- Using a production WSGI server like Gunicorn
- Setting up environment variables
- Using a reverse proxy like Nginx
- Deploying to platforms like Heroku, Vercel, or DigitalOcean

## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Styling:** Custom CSS with modern design principles
- **Icons:** Font Awesome
- **Fonts:** Inter (Google Fonts)

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

Feel free to reach out if you have any questions or suggestions! 