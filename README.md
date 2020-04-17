 Notas: 
    El campo account_id es requerido por el sistema... Buscar manera de obviarlo

 # Definimos la funcionalidad del botón Stop y calculamos el tiempo total
    @api.multi
    def action_stop(self):
        # Comparamos la fecha actual con la fecha de Start, convirtiendola en String
        datetime_diff = datetime.now() - datetime.strptime(self.date_start, DEFAULT_SERVER_DATETIME_FORMAT)
        # Convertimos los segundos totales entre Start y Stop en minutos
        minutes, seconds = divmod(datetime_diff.total_seconds(), 60)
        # Convertimos los minutos en horas
        hours, minutes = divmod(minutes, 60)
        dur_hours = (_('%0*d')%(2,hours))
        dur_minutes = (_('%0*d')%(2,minutes*1.677966102))
        duration = dur_hours+'.'+dur_minutes

        # Revisar que no esté cogiendo el nombre del Ticket en lugar de la descripción
        if not self.running_work_description:
            raise UserError(_('Please enter work description before stopping task.'))

        self.write({
            'timesheet_ids': [(0, 0, {
                'name': self.running_work_description,
                'user_id': self.env.user.id,
                'start_stop': False,
                'date_start': self.date_start,
                'date_stop': datetime.now(),
                'unit_amount': float(duration),
                # Revisar si es necesario especificar el ticket_id
                #'ticket_id': self.id,
             })]
        # Imprime un mensaje en el chatter
        message = _("Stopped by %s.") % (self.env.user.name)
        self.message_post(body=mensaje) 
        return True





    # Imprime un mensaje en el chatter
        #message = _("Started by %s.") % (self.env.user_id)
       # self.message_post('Hello again!', subject='Hello', subtype='mail.mt_comment')   ')