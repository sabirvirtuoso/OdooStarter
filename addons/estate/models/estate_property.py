from odoo import fields, models


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Housing Estate'

    active = fields.Boolean(default=True)

    name = fields.Char('Title', required=True)
    description = fields.Text('Description', required=True)
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Available from', copy=False,
                                    default=lambda self: fields.Datetime.add(fields.Datetime.today(), months=+3))

    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)

    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer('Living Area(sqm)')
    facades = fields.Integer()

    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer('Garden Area(sqm)')
    garden_orientation = fields.Selection(selection=[('north', 'North'), ('south', 'South'),
                                                     ('east', 'East'), ('west', 'West')])

    state = fields.Selection(selection=[('new', 'New'), ('offer received', 'Offer Received'),
                                        ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'),
                                        ('cancelled', 'Cancelled')],
                             required=True, copy=False, default='new')

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    property_tag_ids = fields.Many2many("estate.property.tag", string="Property Tags")

    # Buyer
    partner_id = fields.Many2one('res.partner', string="Buyer", copy=False,
                                 default=lambda self: self.env['res.partner'])

    # Salesperson
    user_id = fields.Many2one('res.users', string="Salesman", default=lambda self: self.env.user)

    # Offers
    offer_ids = fields.One2many('estate.property.offer', "property_id", string="Offers")
