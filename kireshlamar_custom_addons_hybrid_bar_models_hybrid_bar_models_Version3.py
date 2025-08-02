from odoo import models, fields

class HybridBarPayment(models.Model):
    _name = "hybrid.bar.payment"
    _description = "Hybrid Bar Payment"

    customer_name = fields.Char("Customer Name", required=True)
    amount = fields.Float("Amount", required=True)
    state = fields.Selection(
        [
            ("pending", "Pending"),
            ("assigned", "Assigned"),
            ("completed", "Completed"),
        ],
        string="State",
        default="pending",
        required=True,
    )