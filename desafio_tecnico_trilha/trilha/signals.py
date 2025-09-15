from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver 
from .models import Step, Trail, ClientProgress

#Este decorador faz com que sempre que um step seja salvo, essa função seja chamada
@receiver(post_save, sender=Step)
def update_trail_steps_on_save(sender, instance, created, **kwargs):
    #Verifica se um novo step foi criado e não apenas atualizado.
    if created:
        #Acessa a trilha através da instância que representa o step que foi salvo.
        trail = instance.trail 
        #Conta quantos steps estão relacionadas a trail e atribui ao campo number_of_step da trail
        trail.number_of_steps = trail.steps.count()
        #Salva a alteração
        trail.save(update_fields=['number_of_steps'])

@receiver(post_delete, sender=Step)
def update_trail_steps_on_delete(sender, instance, **kwargs):
    trail = instance.trail
    trail.number_of_steps = trail.steps.count()
    trail.save(update_fields=['number_of_steps'])

@receiver(post_save, sender=ClientProgress)
def check_trail_completion(sender, instance, created, **kwars):
    #Verifica se a variável que indica conclusão da sessão é true, para verificar 
    #se a trilha foi finalizada, ou se foi apenas um step.  
    if instance.completed:
        progress = instance
        client_progress = progress.client
        trail = progress.step.trail

        total_step = trail.number_of_steps

        complete_steps = ClientProgress.objects.filter(
            client=client_progress,
            step__trail=trail,
            completed=True
        ).count()

        if total_step > complete_steps:
            current_step = instance.step.order
            next_step = Step.objects.filter(
                order=current_step+1,
                trail=trail
            ).first()
            if next_step:
                print(f"O ID DO PRÒXIMO STEP É: {next_step}")
                ClientProgress.objects.create(
                    client=client_progress,
                    step=next_step,
                    trail=trail,
                    completed=False  # o novo step ainda não foi completado
                )                 



        