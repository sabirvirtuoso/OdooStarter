from odoo import fields, models, api


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'

    price = fields.Float()

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(string="Deadline", compute='_compute_deadline', inverse='_inverse_deadline')
    status = fields.Selection(selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)

    partner_id = fields.Many2one('res.partner', string="Buyer", required=True)
    property_id = fields.Many2one('estate.property', string="Property", required=True)

    # -------------------------------------------------------------------------
    # COMPUTE METHODS
    # -------------------------------------------------------------------------

    @api.depends('create_date', 'validity')
    def _compute_deadline(self):
        for offer in self:
            offer.date_deadline = fields.Datetime.add(
                fields.Datetime.today() if offer.create_date is None else offer.create_date, days=+offer.validity)

    def _inverse_deadline(self):
        for offer in self:
            offer.validity = (fields.Datetime.to_datetime(offer.date_deadline) - fields.Datetime.to_datetime(
                fields.Datetime.today() if offer.create_date is None else offer.create_date)).days
