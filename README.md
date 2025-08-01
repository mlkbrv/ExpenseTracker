# ExpenseTracker

A modern, responsive web application for tracking personal expenses built with Django and styled with Tailwind CSS.

## 📋 Overview

ExpenseTracker is a full-featured expense management application that allows users to add, edit, and delete expenses while providing comprehensive analytics and insights into spending patterns. The application features a clean, modern interface with real-time expense tracking and detailed financial summaries.

## ✨ Features

### Core Functionality
- **Add Expenses**: Simple form to add new expenses with name, amount, and category
- **Edit Expenses**: Modify existing expense entries
- **Delete Expenses**: Remove unwanted expense records
- **Real-time Analytics**: View spending patterns across different time periods

### Analytics & Insights
- **Total Expenses**: Overall spending summary
- **Time-based Analysis**: 
  - Last 365 days spending
  - Last 30 days spending  
  - Last 7 days spending
- **Daily Spending Breakdown**: Track expenses by date
- **Category-wise Analysis**: View spending by expense categories

### User Interface
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Modern UI**: Clean, intuitive interface built with Tailwind CSS
- **Visual Icons**: Edit and delete buttons with intuitive icons
- **Formatted Numbers**: Currency values displayed with proper formatting

## 🛠️ Technology Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite3
- **Frontend**: HTML5, Tailwind CSS 2.2.16
- **Template Engine**: Django Templates
- **Static Assets**: CSS, PNG images for icons

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Node.js and npm (for Tailwind CSS build)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ExpenseTracker
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install django
   ```

4. **Install Node.js dependencies**
   ```bash
   npm install
   ```

5. **Build Tailwind CSS**
   ```bash
   npm run build
   ```

6. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000/`

## 🚀 Usage

### Adding Expenses
1. Navigate to the main page
2. Fill in the expense form with:
   - **Name**: Description of the expense
   - **Amount**: Cost in dollars
   - **Category**: Type of expense (e.g., Food, Transport, Entertainment)
3. Click "Add" to save the expense

### Managing Expenses
- **Edit**: Click the edit icon next to any expense to modify its details
- **Delete**: Click the delete button to remove an expense permanently

### Viewing Analytics
The dashboard automatically displays:
- Total expenses across all time periods
- Spending breakdown for the last 365 days, 30 days, and 7 days
- Daily expense summaries
- Category-wise spending analysis

## 📁 Project Structure

```
ExpenseTracker/
├── ExpenseTracker/          # Django project settings
│   ├── settings.py         # Django configuration
│   ├── urls.py            # Main URL routing
│   └── wsgi.py           # WSGI application
├── myapp/                 # Main Django application
│   ├── models.py         # Database models
│   ├── views.py          # View logic and business logic
│   ├── forms.py          # Form definitions
│   ├── admin.py          # Django admin configuration
│   ├── static/           # Static files (CSS, images)
│   └── templates/        # HTML templates
├── manage.py             # Django management script
├── db.sqlite3           # SQLite database
├── package.json         # Node.js dependencies
└── README.md           # This file
```

## 🗄️ Database Schema

### Expense Model
- `name` (CharField): Description of the expense
- `amount` (IntegerField): Cost amount in dollars
- `category` (CharField): Expense category
- `date` (DateField): Date of the expense (auto-generated)

## 🎨 Customization

### Styling
The application uses Tailwind CSS for styling. To modify the appearance:
1. Edit `myapp/static/myapp/source.css`
2. Run `npm run build` to compile changes

### Adding New Features
- **New Models**: Add to `myapp/models.py`
- **New Views**: Add to `myapp/views.py`
- **New Templates**: Create in `myapp/templates/myapp/`
- **New URLs**: Add to `myapp/urls.py`

## 🔧 Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
```

### Applying Migrations
```bash
python manage.py migrate
```

### Creating Superuser
```bash
python manage.py createsuperuser
```

## 📝 License

This project is licensed under the ISC License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For support and questions, please open an issue in the repository.

---

**Note**: This is a development project. For production deployment, ensure to:
- Change `DEBUG = False` in settings.py
- Use a production database (PostgreSQL, MySQL)
- Configure proper security settings
- Set up static file serving
- Use environment variables for sensitive data 