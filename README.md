# 🏋️ PulseFit — Gym Membership Management System

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1.2-green.svg?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Database](https://img.shields.io/badge/Database-SQLite3-lightgrey.svg?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![UI Style](https://img.shields.io/badge/Design-Glassmorphic%20Dark%20Mode-violet.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-orange.svg)](#)

A modern, responsive, and full-featured Python web application engineered for fitness clubs, gyms, and health studios. Built with **Django (MVT Architecture)** and an embedded **SQLite3** database, it streamlines member lifecycles, automates subscription expiry alerts, provides an interactive reception attendance kiosk, generates printable digital VIP cards, and includes scientific fitness assessment tools.

---

## 🌟 Key Highlights & Features

### 📊 1. Real-Time Operations Dashboard
- **Live Metrics**: Total Members, Active Subscriptions, Expired Accounts, and Today's Check-Ins.
- **Financial Analytics**: Total revenue aggregated dynamically via Django ORM.
- **7-Day Expiry Forecast**: Proactive alerts for memberships lapsing within the next 7 days, complete with quick-action renewal shortcuts.
- **Live Activity Feed**: Real-time log of members currently on the gym floor.

### 👥 2. Member Management (Full CRUD)
- **Automated Lifecycle**: Auto-generates branded IDs (`PF-1001`, `PF-1002`) and computes end dates based on selected plans.
- **Search & Filters**: Instant multi-parameter search (Name, Phone, Email, Member ID) with filter tabs for status (*Active*, *Expiring Soon*, *Expired*).
- **1-Click Renewal Engine**: Dynamic extension by 1, 3, 6, or 12 months (extends active memberships or restarts from today for expired ones).
- **Profile Customization**: Assign dedicated coaches, emergency contacts, medical notes, and payment records.

### 🪪 3. Digital VIP Membership Card / Pass
- Generates a branded virtual VIP card with member details, coach assignment, barcode, and QR code visual.
- Includes a dedicated CSS print stylesheet for 1-click physical card printing (`window.print()`).

### ⏱️ 4. Reception Attendance Kiosk
- Dual-mode punch-in: fast Member ID lookup or dropdown selection from active members.
- **Duplicate Prevention**: Database-level `unique_together` constraint guarantees that a member cannot be checked in more than once on the same calendar day.
- Visual warnings if an expired member attempts to check in.

### 🧮 5. Scientific Biometrics & Fitness Tool
- **Body Mass Index (BMI)**: Instant categorization (Underweight, Normal, Overweight, Obese).
- **Mifflin-St Jeor BMR & TDEE**: Daily caloric needs based on activity levels.
- **Macro Guidance**: Automated daily water intake (Liters) and protein targets (grams).

### 🔐 6. Django Administration Portal
- Pre-configured admin interface at `/admin/` with custom filters, search fields, and date hierarchy navigation for Plans, Members, and Attendance.

---

## 🛠️ Technology Stack

| Layer | Technologies Used |
|---|---|
| **Backend Framework** | Python 3.13, Django 6.1.2 (MVT Pattern) |
| **Database** | SQLite3 (Zero-configuration relational database) |
| **Frontend** | HTML5, Vanilla CSS3 (Custom Glassmorphism, Dark Mode), JavaScript (ES6) |
| **Icons & Typography** | FontAwesome 6, Google Fonts (*Outfit* & *Plus Jakarta Sans*) |

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.10 or higher installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/gym-membership-management-system.git
cd gym-membership-management-system
