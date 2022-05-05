from flask import Blueprint, jsonify, request
from json import dumps, dump
from api.models.db import db
from api.models.transaction import Transaction
from sqlalchemy import func

transactions = Blueprint('transactions', 'transactions')

#### Transactions ####
@transactions.route('/', methods=["POST"])
def create():
  data = request.get_json()
  transaction = Transaction(**data)
  db.session.add(transaction)
  db.session.commit()
  return jsonify(transaction.serialize()), 201


@transactions.route('/', methods=["GET"])
def getAll():  
  transactions = Transaction.query.all()
  return jsonify([transaction.serialize() for transaction in transactions]), 200

@transactions.route('/total', methods=["GET"])
def getTransactionTotal():
  transaction_total = Transaction.query.with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  cash_total = Transaction.query.filter_by(sale_type='cash').with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  loan_total = Transaction.query.filter_by(sale_type='loan').with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  print('loan_type filtered: cash', loan_total)
  # cash_total = Transaction.query.
  print('Transaction Total: ', transaction_total, type(transaction_total))
  return jsonify(transaction_total, cash_total, loan_total)

@transactions.route('/total/community/<id>')
def getCommunityTransactionTotal(id):
  transaction_total = Transaction.query.filter_by(community_id=id).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  cash_total = Transaction.query.filter_by(sale_type='cash', community_id=id).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  loan_total = Transaction.query.filter_by(sale_type='loan', community_id=id).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  return jsonify(transaction_total, cash_total, loan_total)


@transactions.route('/total/department/<id>')
def getCountryTransactionTotal(id):
  transaction_total = Transaction.query.filter_by(department_id=id).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  cash_total = Transaction.query.filter_by(sale_type='cash', department_id=id).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  loan_total = Transaction.query.filter_by(sale_type='loan', department_id=id).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  return jsonify(transaction_total, cash_total, loan_total)