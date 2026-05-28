import streamlit as st
from Personal_Finance_Expense import whole_processor
import pandas as pd
import json
import os
import datetime

JSONFILE = "Personal_Finance_Expense.json"
TXTFILE = "Personal_Finance_Expense.txt"


def _ensure_json():
    if not os.path.exists(JSONFILE):
        with open(JSONFILE, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=2)


def _migrate_from_txt():
    if not os.path.exists(TXTFILE):
        return
    try:
        with open(TXTFILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except IOError:
        return
    entries = []
    for line in lines[1:]:
        parts = line.strip().split("\t")
        if len(parts) < 4:
            continue
        typ = parts[0].strip()
        cat = parts[1].strip()
        dt = parts[2].strip()
        try:
            amt = float(parts[3])
        except ValueError:
            continue
        entries.append({"type": typ, "category": cat, "datetime": dt, "amount": amt})
    if entries:
        _ensure_json()
        data = _load_data()
        data.extend(entries)
        _save_data(data)


def _load_data():
    _ensure_json()
    _migrate_from_txt()
    try:
        with open(JSONFILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def _save_data(data):
    with open(JSONFILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_income(category, amount):
    if not str(category).strip():
        raise ValueError("Category cannot be empty.")
    try:
        amt = float(amount)
        if amt < 0:
            raise ValueError("Amount cannot be negative.")
    except (TypeError, ValueError):
        raise ValueError("Invalid amount — please provide a number.")
    entry = {"type": "Income", "category": str(category).strip(), "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "amount": amt}
    data = _load_data()
    data.append(entry)
    _save_data(data)


def add_expense(category, amount):
    if not str(category).strip():
        raise ValueError("Category cannot be empty.")
    try:
        amt = float(amount)
        if amt < 0:
            raise ValueError("Amount cannot be negative.")
    except (TypeError, ValueError):
        raise ValueError("Invalid amount — please provide a number.")
    entry = {"type": "Expense", "category": str(category).strip(), "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "amount": amt}
    data = _load_data()
    data.append(entry)
    _save_data(data)


def get_summary():
    data = _load_data()
    total_income = 0.0
    total_expense = 0.0
    for item in data:
        typ = str(item.get("type", "")).strip().lower()
        try:
            amount = float(item.get("amount", 0))
        except (TypeError, ValueError):
            continue
        if typ == "income":
            total_income += amount
        elif typ == "expense":
            total_expense += amount
    return {"total_income": total_income, "total_expense": total_expense, "balance": total_income - total_expense}


def main():
    st.title("Personal Finance Expense Tracker")
    o = whole_processor()

    menu = st.sidebar.radio("Choose action:", ["Dashboard", "Add Income", "Add Expense", "View Data"])

    if menu == "Add Income":
        st.header("Add Income")
        with st.form("income_form"):
            category = st.text_input("Category")
            amount = st.number_input("Amount", min_value=0.0, format="%.2f")
            submitted = st.form_submit_button("Add Income")
            if submitted:
                try:
                    o.add_income(category, amount)
                    st.success("Income added")
                except Exception as e:
                    st.error(str(e))

    elif menu == "Add Expense":
        st.header("Add Expense")
        with st.form("expense_form"):
            category = st.text_input("Category")
            amount = st.number_input("Amount", min_value=0.0, format="%.2f")
            submitted = st.form_submit_button("Add Expense")
            if submitted:
                try:
                    o.add_expense(category, amount)
                    st.success("Expense added")
                except Exception as e:
                    st.error(str(e))

    elif menu == "View Data":
        st.header("All Records")
        data = o.get_data()
        if not data:
            st.info("No records found.")
        else:
            df = pd.DataFrame(data)
            st.dataframe(df)

    else:  # Dashboard
        st.header("Summary")
        s = o.get_summary()
        st.metric("Total Income", f"{s['total_income']:.2f}")
        st.metric("Total Expense", f"{s['total_expense']:.2f}")
        st.metric("Balance", f"{s['balance']:.2f}")


if __name__ == '__main__':
    main()
