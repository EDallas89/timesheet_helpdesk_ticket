          <field name="timesheet_ids" context="{'default_project_id': project_id}">
            <tree editable="bottom">
              <!--<field name="date" />-->
              <!--required="1"-->
              <field name="user_id" options="{&quot;no_open&quot;: True}" />
              <field name="name" />
              <field name="date_start" />
              <field name="date_stop" />
              <field name="unit_amount" string="Duration" sum="Total time" widget="float_time" />
            </tree>
          </field>


          #class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    date_start = fields.Datetime('Start Time')
    date_stop = fields.Datetime('End Time')
    ticket_id = fields.Many2one('acs.support.ticket', string="Support Ticket")



    =================Botones================
     <xpath expr="//field[@name='number']" position="before">
        <div class="oe_button_box" name="button_box">
          <!-- attrs="{'invisible': [('start_stop', '=', True)]}"-->
          <button name="action_start" string="Start" type="object" class="oe_inline oe_stat_button" icon="fa-play" />
          <!-- attrs="{'invisible': [('start_stop', '=', False)]}"-->
          <button name="action_stop" string="Stop" type="object" class="oe_stat_button oe_inline" icon="fa-stop" />
        </div>
      </xpath>