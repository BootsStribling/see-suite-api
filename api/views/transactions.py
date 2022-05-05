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
  return jsonify(transaction_total, cash_total, loan_total)

@transactions.route('/total/distributors')
def getDistributorTransactionTotal():
  transaction_total = Transaction.query.filter_by(distributor=1).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  cash_total = Transaction.query.filter_by(sale_type='cash', distributor=1).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  loan_total = Transaction.query.filter_by(sale_type='loan', distributor=1).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  return jsonify(transaction_total, cash_total, loan_total)

@transactions.route('/total/community/<id>')
def getCommunityTransactionTotal(id):
  transaction_total = Transaction.query.filter_by(community_id=id).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  cash_total = Transaction.query.filter_by(sale_type='cash', community_id=id).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  loan_total = Transaction.query.filter_by(sale_type='loan', community_id=id).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  return jsonify(transaction_total, cash_total, loan_total)


@transactions.route('/total/department/<id>')
def getDepartmentTransactionTotal(id):
  transaction_total = Transaction.query.filter_by(department_id=id).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  cash_total = Transaction.query.filter_by(sale_type='cash', department_id=id).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  loan_total = Transaction.query.filter_by(sale_type='loan', department_id=id).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  return jsonify(transaction_total, cash_total, loan_total)

@transactions.route('/total/country/<id>')
def getCountryTransactionTotal(id):
  transaction_total = Transaction.query.filter_by(country_id=id).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  cash_total = Transaction.query.filter_by(sale_type='cash', country_id=id).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  loan_total = Transaction.query.filter_by(sale_type='loan', country_id=id).with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  return jsonify(transaction_total, cash_total, loan_total)


# All in country 1, all transactions are 1 dollar
# Department 1
  # Communities -  Total 20
  #   1: 5 loans, 5 cash output: [20,10,10]
  #   2: 5 loans, 5 cash

#Department 2
  # Communities- Total 4
    # 3: 1 loans, 1 cash
    # 4: 1 1oans, 1 cash output: [4,2,2]