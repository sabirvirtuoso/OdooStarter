from odoo import fields, models, api


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'

    name = fields.Char(required=True)
    sequence = fields.Integer("Sequence", default=1)

    property_ids = fields.One2many('estate.property', "property_type_id", string="Properties")

    offer_ids = fields.One2many('estate.property.offer', "property_type_id", string="Offers")
    offer_count = fields.Integer(compute='_compute_offer_count')

    # _sql_constraints = ['unique_property_type', 'UNIQUE (name)', 'The property type should be unique']

    # can use default_order attribute in tree view
    _order = "sequence, name"

    # -------------------------------------------------------------------------
    # COMPUTE METHODS
    # -------------------------------------------------------------------------

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for type in self:
            type.offer_count = len(type.offer_ids)
