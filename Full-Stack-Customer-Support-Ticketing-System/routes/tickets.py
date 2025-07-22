from flask import Flask,Blueprint

tickets_bp=Blueprint('tickets',__name__)

@tickets_bp.route('/ticket')
def tickets():
    return {'Tickets status : ':'Booked'}
