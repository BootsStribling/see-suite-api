from flask import Blueprint, jsonify, request
from json import dumps, dump
from api.models.db import db
from api.models.transaction import Transaction

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