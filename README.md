# PayrollPH — Payroll Management System

A full-featured payroll management system built with **Flask + SQLite3**, designed for Philippine businesses with mobile-friendly GPS time tracking, automated payroll computation, and printable payslips.

---

## 🗂 Project Structure

```
payroll_system/
├── run.py                          # Entry point
├── requirements.txt
├── README.md
├── instance/
│   └── payroll.db                  # SQLite3 database (auto-created)
└── app/
    ├── __init__.py                 # App factory, blueprint registration
    ├── database.py                 # DB init, schema, seeding
    ├── auth_helpers.py             # Decorators, payroll computation
    ├── blueprints/
    │   ├── auth.py                 # Login / logout
    │   ├── admin.py                # Admin: employees, attendance, payroll
    │   ├── employee.py             # Employee: dashboard, attendance, payslip
    │   └── api.py                  # REST API: time-in, time-out, GPS
    └── templates/
        ├── base.html               # Shared layout with sidebar
        ├── auth/
        │   └── login.html
        ├── admin/
        │   ├── dashboard.html
        │   ├── employees.html
        │   ├── employee_form.html
        │   ├── attendance.html
        │   ├── payroll.html
        │   ├── payslip.html
        │   └── map.html            # Leaflet.js location map
        └── employee/
            ├── dashboard.html      # Time-in/out with GPS
            ├── attendance.html
            ├── payslips.html
            └── payslip.html
```

---

## 🚀 Setup & Running

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the server
```bash
python run.py
```

### 3. Open in browser
```
http://localhost:5000
```

---

## 🔐 Demo Credentials

| Role     | Username  | Password |
|----------|-----------|----------|
| Admin    | admin     | admin123 |
| Employee | jdcruz    | emp123   |
| Employee | mrsantos  | emp123   |
| Employee | alreyes   | emp123   |
| Employee | bnlim     | emp123   |

---

## 📦 Features

### 🔐 Authentication
- Secure login/logout with `werkzeug.security` password hashing
- Role-based access: **Admin** (full control) / **Employee** (self-service)
- Session-based auth with Flask sessions

### 👨‍💼 Employee Management (Admin)
- Add, edit, deactivate employees
- Fields: Employee Code, Full Name, Position, Department
- Rate type: Daily or Hourly salary rates
- Government IDs: SSS, PhilHealth, Pag-IBIG, TIN
- Username & password per employee

### ⏱ Time Tracking (Employee)
- One-tap **Time In** / **Time Out** from mobile or desktop
- GPS coordinates captured via HTML5 Geolocation API
- Sent to `/api/time-in` and `/api/time-out` via fetch/AJAX
- Late detection (cutoff: 08:00 AM) and minute calculation

### 📍 GPS Location Logging
- Coordinates stored per time-in and time-out event
- Admin map view using **Leaflet.js** (OpenStreetMap)
- Green dots = time-in, red dots = time-out, blue lines = path
- Clickable Google Maps links in attendance table

### 💰 Payroll Computation
- Supports both **daily** and **hourly** rate types
- Automatic computation:
  - Basic pay based on days/hours worked
  - Overtime pay at **125%** (PH standard)
  - Late deduction per minute
  - SSS (~4.5% employee share, max ₱1,125)
  - PhilHealth (2.5% employee share, max ₱2,500)
  - Pag-IBIG (2%, max ₱100)
  - Withholding tax (graduated PH tax brackets)
- Admin selects period and employees; generates in bulk

### 📄 Payslip
- Itemized view: gross, overtime, all deductions, net pay
- Print-ready (CSS print media query hides navigation)
- Admin can view/print any payslip; employees see only their own released payslips

### 🗄 Database Schema (SQLite3)
- **users** — authentication credentials and roles
- **employees** — profile, position, compensation, government IDs
- **attendance** — time-in/out, GPS coordinates, computed hours, late flags
- **payroll** — computed pay runs per employee per period

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/time-in` | Record time-in with GPS |
| POST | `/api/time-out` | Record time-out with GPS |
| GET | `/api/attendance/today` | Get today's record (employee) |
| GET | `/api/attendance/locations?date=` | GPS data for map (admin) |
| GET | `/api/employees` | List all employees (admin) |
| POST | `/api/payroll/generate` | Generate payroll programmatically |

All API endpoints return JSON. Authentication uses Flask sessions (cookie-based).

---

## 🔒 Security Notes
- Passwords stored as bcrypt hashes via `werkzeug.security`
- Route-level decorators: `@admin_required`, `@login_required`
- Foreign keys enforced in SQLite3 (`PRAGMA foreign_keys = ON`)
- Session cleared on logout

---

## 💡 Extending the System
- **Export to Excel/PDF**: add `openpyxl` or `reportlab` and a `/admin/payroll/export` route
- **Email payslips**: integrate Flask-Mail
- **Real-time notifications**: add Flask-SocketIO
- **REST API auth**: replace sessions with JWT (`flask-jwt-extended`)
