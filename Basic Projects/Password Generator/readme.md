# 🔑 Password Generator

A **Python-based password generator** that creates **secure passwords** based on user-defined strength levels:  
✔ **Weak** (Lowercase letters)  
✔ **Medium** (Uppercase + Numbers)  
✔ **Strong** (Uppercase + Numbers + Symbols)  
✔ **Very Strong** (Minimum 12 characters with a mix of all types)

---

## 🚀 Features

✅ Generate **random passwords** with different security levels  
✅ Customize **password length**  
✅ Ensures **strong password policies**  
✅ **Simple & lightweight** – Runs in the terminal  
✅ Uses Python’s built-in **`random`** & **`string`** modules

---

## ⚙️ How It Works?

1️⃣ Run the script  
2️⃣ Enter the **password strength** (weak/medium/strong/very strong)  
3️⃣ Enter the **password length**  
4️⃣ The script generates a **secure password**

---

## 📝 Code Explanation

🔹 **Character Sets Used:**

- `string.ascii_lowercase` → Lowercase letters (`abcdefghijklmnopqrstuvwxyz`)
- `string.ascii_uppercase` → Uppercase letters (`ABCDEFGHIJKLMNOPQRSTUVWXYZ`)
- `string.digits` → Numbers (`0123456789`)
- `string.punctuation` → Symbols (`!@#$%^&*()_+[]{}` etc.)

🔹 **Password Strength Logic:**

| Strength Level  | Includes                                                 | Default Length |
| --------------- | -------------------------------------------------------- | -------------- |
| **Weak**        | Lowercase only                                           | 8              |
| **Medium**      | Lowercase + Uppercase + Numbers                          | 8              |
| **Strong**      | Lowercase + Uppercase + Numbers + Symbols                | 8              |
| **Very Strong** | Lowercase + Uppercase + Numbers + Symbols (min 12 chars) | 12+            |

---

## 🖥 Installation & Usage

📌 **Run the script:**

```bash
python password_generator.py
```

### Example Input and Output

```
Enter password strength (weak/medium/strong/very strong): strong
Enter password length: 10
Generated strong password: G$9r@T!q3P
```

---

🔹 Happy Coding! 🔐 🚀
