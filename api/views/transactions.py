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

# @transactions.route('/total', methods=["GET"])
# def getTransactionTotal():
#   transactions = Transaction.query.with_entities(Transaction.transaction_total).all()
#   print(transactions)
#   return dump([transaction for transaction in transactions])

@transactions.route('/total', methods=["GET"])
def getTransactionTotal():
  transaction_total = Transaction.query.with_entities(func.sum(Transaction.transaction_total).label('total')).first().total
  print('Transaction Total: ', transaction_total, type(transaction_total))
  return jsonify(transaction_total)