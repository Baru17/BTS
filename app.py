# # from flask import Flask, render_template, request, redirect
# # from flask_mysqldb import MySQL

# # app = Flask(__name__)

# # # MySQL configuration
# # app.config['MYSQL_HOST'] = 'localhost'
# # app.config['MYSQL_USER'] = 'root'
# # app.config['MYSQL_PASSWORD'] = '@Barani17@'
# # app.config['MYSQL_DB'] = 'bus_tracking'

# # mysql = MySQL(app)

# # # Registration page
# # @app.route('/register', methods=['GET','POST'])
# # def register():
# #     if request.method == 'POST':
# #         name = request.form['name']
# #         email = request.form['email']
# #         password = request.form['password']
# #         bus_number = request.form['bus_number']

# #         cursor = mysql.connection.cursor()
# #         cursor.execute('INSERT INTO users (name, email,password, bus_number) VALUES (%s,%s,%s,%s)', (name, email,password,  bus_number))
# #         mysql.connection.commit()
# #         cursor.close()

# #         return "User registered successfully!"

# #     return render_template('register.html')

# # # Admin dashboard to display users
# # @app.route('/admin')
# # def admin_dashboard():
# #     cursor = mysql.connection.cursor()
# #     cursor.execute('SELECT name, email,password, bus_number FROM users')
# #     users = cursor.fetchall()
# #     cursor.close()

# #     return render_template('admin.html', users=users)

# # if __name__ == '__main__':
# #     app.run(debug=True)


# from flask import Flask, render_template, request
# from flask_mysqldb import MySQL
# import MySQLdb.cursors

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # MySQL configuration
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'         # your MySQL username
# app.config['MYSQL_PASSWORD'] = '@Barani17@'         # your MySQL password
# app.config['MYSQL_DB'] = 'bus_tracking'    # your database name

# mysql = MySQL(app)

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     error = ''
#     success = ''
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         confirm = request.form['confirm']
#         bus_number = request.form['bus_number']

#         # Password validation
#         if password != confirm:
#             error = "Passwords do not match."
#             return render_template('register.html', error=error, success=success)

#         # Check if email already exists
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
#         account = cursor.fetchone()
#         if account:
#             error = "Email already registered."
#             cursor.close()
#             return render_template('register.html', error=error, success=success)

#         # Insert into database
#         try:
#             cursor.execute("INSERT INTO users (name, email, bus_number) VALUES (%s, %s, %s)",
#                            (name, email, bus_number))
#             mysql.connection.commit()
#             cursor.close()
#             success = "Registration successful!"
#         except Exception as e:
#             cursor.close()
#             error = f"Database error: {str(e)}"

#     return render_template('register.html', error=error, success=success)

# if __name__ == '__main__':
#     app.run(debug=True)


# @app.route('/admin')
# def admin_dashboard():
#      cursor = mysql.connection.cursor()
#      cursor.execute('SELECT name, email,password, bus_number FROM users')
#      users = cursor.fetchall()
#      cursor.close()
#      return render_template('admin.html', users=users)

# if __name__ == '__main__':
#      app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# import hashlib

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # MySQL configuration
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '@Barani17@'
# app.config['MYSQL_DB'] = 'bus_tracking'

# mysql = MySQL(app)

# # ------------------- User Registration -------------------
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     error = ''
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         confirm = request.form['confirm']
#         bus_number = request.form['bus_number']

#         if password != confirm:
#             error = "Passwords do not match."
#             return render_template('register.html', error=error)

#         hashed_password = hashlib.sha256(password.encode()).hexdigest()

#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
#         account = cursor.fetchone()
#         if account:
#             cursor.close()
#             error = "Email already registered."
#             return render_template('register.html', error=error)

#         try:
#             cursor.execute(
#                 "INSERT INTO users (name, email, password, bus_number) VALUES (%s, %s, %s, %s)",
#                 (name, email, hashed_password, bus_number)
#             )
#             mysql.connection.commit()
#             cursor.close()
#             return redirect(url_for('login'))
#         except Exception as e:
#             cursor.close()
#             error = f"Database error: {str(e)}"

#     return render_template('register.html', error=error)

# # ------------------- User Login -------------------
# @app.route('/', methods=['GET', 'POST'])
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = ''
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         hashed_password = hashlib.sha256(password.encode()).hexdigest()

#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, hashed_password))
#         user = cursor.fetchone()
#         cursor.close()

#         if user:
#             return redirect(url_for('home'))
#         else:
#             error = "Invalid email or password."

#     return render_template('index.html', error=error)

# # ------------------- Forgot Password -------------------
# @app.route('/forgetpassword', methods=['GET', 'POST'])
# def forget_password():
#     error = ''
#     if request.method == 'POST':
#         email = request.form['email']
#         new_password = request.form['password']
#         hashed_password = hashlib.sha256(new_password.encode()).hexdigest()

#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
#         user = cursor.fetchone()

#         if user:
#             cursor.execute("UPDATE users SET password=%s WHERE email=%s", (hashed_password, email))
#             mysql.connection.commit()
#             cursor.close()
#             flash("Password updated successfully! Please login.", "success")
#             return redirect(url_for('login'))
#         else:
#             cursor.close()
#             error = "Email not found."
#             return render_template('forgetpassword.html', error=error)

#     return render_template('forgetpassword.html')

# # ------------------- Home Page -------------------
# @app.route('/home')
# def home():
#     return render_template('home.html')

# # ------------------- Admin -------------------
# @app.route('/adminlog')
# def admin_login():
#     return render_template('adminlog.html')

# @app.route('/admin.dashboard')
# def admindashboard():
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cursor.execute("SELECT id, name, email, bus_number FROM users")
#     users = cursor.fetchall()
#     cursor.close()
#     return render_template('admin.dashboard.html', users=users)

# @app.route('/delete_user/<int:user_id>', methods=['POST'])
# def delete_user(user_id):
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     try:
#         cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
#         mysql.connection.commit()
#         cursor.close()
#         return {"success": True}
#     except:
#         cursor.close()
#         return {"success": False}

# # ------------------- Other Pages -------------------
# @app.route('/buses')
# def buses():
#     return render_template('buses.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/drivers')
# def drivers():
#     return render_template('drivers.html')

# # ------------------- Bus Tracking -------------------
# @app.route('/tracking/<int:bus_number>')
# def tracking(bus_number):
#     # You can fetch bus-specific data from MySQL here if needed
#     return render_template('tracking.html', bus_number=bus_number)

# # ------------------- Run App -------------------
# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# from flask_bcrypt import Bcrypt

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # MySQL configuration
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '@Barani17@'
# app.config['MYSQL_DB'] = 'bus_tracking'

# mysql = MySQL(app)
# bcrypt = Bcrypt(app)

# # ------------------- User Registration -------------------
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     error = ''
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         confirm = request.form['confirm']
#         bus_number = request.form['bus_number']

#         if password != confirm:
#             error = "Passwords do not match."
#             return render_template('register.html', error=error)

#         # Hash the password using bcrypt
#         hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
#         account = cursor.fetchone()
#         if account:
#             cursor.close()
#             error = "Email already registered."
#             return render_template('register.html', error=error)

#         try:
#             cursor.execute(
#                 "INSERT INTO users (name, email, password, bus_number) VALUES (%s, %s, %s, %s)",
#                 (name, email, hashed_password, bus_number)
#             )
#             mysql.connection.commit()
#             cursor.close()
#             return redirect(url_for('login'))
#         except Exception as e:
#             cursor.close()
#             error = f"Database error: {str(e)}"

#     return render_template('register.html', error=error)

# # ------------------- User Login -------------------
# @app.route('/', methods=['GET', 'POST'])
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = ''
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
#         user = cursor.fetchone()
#         cursor.close()

#         if user and bcrypt.check_password_hash(user['password'], password):
#             return redirect(url_for('home'))
#         else:
#             error = "Invalid email or password."

#     return render_template('index.html', error=error)

# # ------------------- Forgot Password -------------------
# @app.route('/forgetpassword', methods=['GET', 'POST'])
# def forget_password():
#     error = ''
#     if request.method == 'POST':
#         email = request.form['email']
#         new_password = request.form['password']
#         hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')

#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
#         user = cursor.fetchone()

#         if user:
#             cursor.execute("UPDATE users SET password=%s WHERE email=%s", (hashed_password, email))
#             mysql.connection.commit()
#             cursor.close()
#             flash("Password updated successfully! Please login.", "success")
#             return redirect(url_for('login'))
#         else:
#             cursor.close()
#             error = "Email not found."
#             return render_template('forgetpassword.html', error=error)

#     return render_template('forgetpassword.html')

# # ------------------- Home Page -------------------
# @app.route('/home')
# def home():
#     return render_template('home.html')

# # ------------------- Admin -------------------
# @app.route('/adminlog')
# def admin_login():
#     return render_template('adminlog.html')

# @app.route('/admin.dashboard')
# def admindashboard():
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cursor.execute("SELECT id, name, email, bus_number FROM users")
#     users = cursor.fetchall()
#     cursor.close()
#     return render_template('admin.dashboard.html', users=users)

# @app.route('/delete_user/<int:user_id>', methods=['POST'])
# def delete_user(user_id):
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     try:
#         cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
#         mysql.connection.commit()
#         cursor.close()
#         return {"success": True}
#     except:
#         cursor.close()
#         return {"success": False}

# # ------------------- Other Pages -------------------
# @app.route('/buses')
# def buses():
#     return render_template('buses.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/drivers')
# def drivers():
#     return render_template('drivers.html')

# # ------------------- Bus Tracking -------------------
# @app.route('/tracking/<int:bus_number>')
# def tracking(bus_number):
#     # You can fetch bus-specific data from MySQL here if needed
#     return render_template('tracking.html', bus_number=bus_number)

# # ------------------- Run App -------------------
# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# ------------------- Railway MySQL CONFIG -------------------
app.config['MYSQL_HOST'] = 'trolley.proxy.rlwy.net'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'DwivKXURFWpZapyOyWpXllGihAmuOjjS'
app.config['MYSQL_DB'] = 'railway'
app.config['MYSQL_PORT'] = 42579

mysql = MySQL(app)
bcrypt = Bcrypt(app)


# ------------------------------------------------------------
# AUTO-FIX SQL TABLE (CREATES TABLE + FIXES AUTO_INCREMENT)
# ------------------------------------------------------------
def fix_users_table():
    cursor = mysql.connection.cursor()

    # Create table if missing
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            bus_number VARCHAR(50) NOT NULL
        )
    """)

    # Ensure id is auto increment
    cursor.execute("""
        ALTER TABLE users 
        MODIFY id INT NOT NULL AUTO_INCREMENT;
    """)

    mysql.connection.commit()
    cursor.close()


# Run auto-fix when app starts
with app.app_context():
    fix_users_table()


# ------------------- User Registration -------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ''
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']
        bus_number = request.form['bus_number']

        if password != confirm:
            error = "Passwords do not match."
            return render_template('register.html', error=error)

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        account = cursor.fetchone()

        if account:
            cursor.close()
            error = "Email already registered."
            return render_template('register.html', error=error)

        try:
            cursor.execute(
                "INSERT INTO users (name, email, password, bus_number) VALUES (%s, %s, %s, %s)",
                (name, email, hashed_password, bus_number)
            )
            mysql.connection.commit()
            cursor.close()
            flash("Registration successful! Please login.", "success")
            return redirect(url_for('login'))

        except Exception as e:
            cursor.close()
            error = f"Database error: {str(e)}"

    return render_template('register.html', error=error)


# ------------------- Login -------------------
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()
        cursor.close()

        if user and bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['name']
            session['bus_number'] = user['bus_number']

            flash("Login successful!", "success")
            return redirect(url_for('home'))
        else:
            error = "Invalid email or password."

    return render_template('index.html', error=error)


# ------------------- Forget Password -------------------
@app.route('/forgetpassword', methods=['GET', 'POST'])
def forget_password():
    error = ''
    if request.method == 'POST':
        email = request.form['email']
        new_password = request.form['password']

        hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()

        if user:
            cursor.execute(
                "UPDATE users SET password=%s WHERE email=%s",
                (hashed_password, email)
            )
            mysql.connection.commit()
            cursor.close()

            flash("Password updated successfully! Please login.", "success")
            return redirect(url_for('login'))
        else:
            cursor.close()
            error = "Email not found."

    return render_template('forgetpassword.html', error=error)


# ------------------- Home -------------------
@app.route('/home')
def home():
    if 'username' not in session:
        flash("Please log in first.", "error")
        return redirect(url_for('login'))

    return render_template('home.html',
                           username=session['username'],
                           bus_number=session['bus_number'])


# ------------------- Track -------------------
@app.route('/track')
def track():
    if 'bus_number' not in session:
        flash("Please log in first.", "error")
        return redirect(url_for('login'))

    return redirect(url_for('tracking', bus_number=session['bus_number']))


@app.route('/tracking/<int:bus_number>')
def tracking(bus_number):
    if 'bus_number' not in session:
        flash("Please log in first.", "error")
        return redirect(url_for('login'))

    # Registered bus
    registered_bus = int(session['bus_number'])

    # Allow registered bus OR temporary bus
    temp_bus = session.get('temp_bus')

    if bus_number != registered_bus and bus_number != temp_bus:
        flash("You are not allowed to view this bus.", "error")
        return redirect(url_for('home'))

    return render_template('tracking.html', bus_number=bus_number)

@app.route('/set-temp-bus/<int:bus_number>')
def set_temp_bus(bus_number):
    session['temp_bus'] = bus_number
    return redirect(url_for('tracking', bus_number=bus_number))



# ------------------- Admin Login Page -------------------
@app.route('/adminlog')
def admin_login():
    return render_template('adminlog.html')


# ------------------- Admin Dashboard -------------------
@app.route('/admin.dashboard')
def admin_dashboard():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT id, name, email, bus_number FROM users")
    users = cursor.fetchall()
    cursor.close()

    return render_template('admin.dashboard.html', users=users)


# ------------------- Delete User (AJAX) -------------------
@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"success": True})
    except:
        cursor.close()
        return jsonify({"success": False})


# ------------------- Update User (AJAX) -------------------
@app.route('/update_user/<int:user_id>', methods=['POST'])
def update_user(user_id):
    try:
        data = request.get_json(force=True)
        name = data.get("name")
        email = data.get("email")
        bus_number = data.get("bus_number")

        if not (name and email and bus_number):
            return jsonify({"success": False, "error": "All fields are required."})

        cursor = mysql.connection.cursor()
        cursor.execute(
            "UPDATE users SET name=%s, email=%s, bus_number=%s WHERE id=%s",
            (name, email, bus_number, user_id)
        )
        mysql.connection.commit()

        if cursor.rowcount == 0:
            cursor.close()
            return jsonify({"success": False, "error": "User not found."})

        cursor.close()
        return jsonify({"success": True})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


# ------------------- Other Pages -------------------
@app.route('/buses')
def buses():
    if 'bus_number' not in session:
        flash("Please log in first.", "error")
        return redirect(url_for('login'))
    return render_template('buses.html', bus_number=session['bus_number'])


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/drivers')
def drivers():
    return render_template('drivers.html')


# ------------------- Logout -------------------
@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect(url_for('login'))


# ------------------- Run App -------------------
if __name__ == '__main__':
    app.run(debug=True) 
