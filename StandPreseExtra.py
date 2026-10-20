from StandStandard import StandStandard

class StandPreseExtra(StandStandard):

  def __init__(
      self, codice, superficie, padiglione, prezzo_base, numero_prese
  ):
    super().__init__(codice, superficie, padiglione, prezzo_base)
    self.numero_prese = numero_prese

  def calcola_prezzo(self):
    # Sovrapprezzo pari al 7% per ogni presa extra
    return self.prezzo_base * (1 + 0.07 * self.numero_prese)

  def __str__(self):
    stato = (
        f"Assegnato a {self.espositore_assegnato.codice}"
        if self.espositore_assegnato
        else "Disponibile"
    )
    return (
        f"{self.codice}, {self.superficie} mq"
        f" {self.padiglione}, {self.calcola_prezzo():.2f}€"
        f" aggiuntive: {self.numero_prese} - {stato}"
    )