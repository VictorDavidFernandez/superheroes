# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api


class superheroe(models.Model):
    _name = 'superheroes.superheroe'
    name = fields.Char(string="Main Alias", required=True)
    realName = fields.Char(string="Real Name")
    firstAppearance = fields.Date("First Appearance")
    supervillain_id = fields.One2many('superheroes.supervillain', 'superheroe_id', string="supervillain")
    events_ids = fields.Many2many('superheroes.event', 'superheroes_superheroes_events_rel', 'superheroe_id', 'events_id',
                                  'Events')


class supervillain(models.Model):
    _name = 'superheroes.supervillain'
    name = fields.Char(string="Main Alias", required=True)
    realName = fields.Char(string="Real Name")
    firstAppearance = fields.Date("First Appearance")
    superheroe_id = fields.Many2one('superheroes.superheroe', string="superheroe")
    events_ids = fields.Many2many('superheroes.event', 'superheroes_supervillains_events_rel', 'supervillain_id', 'events_id',
                                  'Events')

class event(models.Model):
    _name = 'superheroes.event'
    name = fields.Char(string="Event Name", required=True)
    startDate = fields.Date(string="Start Date")
    endDate = fields.Date(string="End Date")
    duration = fields.Char(string="Days Duration", compute="_get_duration")
    superheroes_ids = fields.Many2many('superheroes.superheroe', 'superheroes_superheroes_events_rel', 'events_id', 'superheroe_id',
                                       'Superheroes')
    supervillains_ids = fields.Many2many('superheroes.supervillain', 'superheroes_supervillains_events_rel', 'events_id', 'supervillain_id',
                                  'Supervillains')

    def _get_duration(self):
        for dur in self:
            startDate = fields.Datetime.to_datetime(dur.startDate).date()
            endDate = fields.Datetime.to_datetime(dur.endDate).date()
            duration = str(int((endDate - startDate).days))
            dur.duration = duration