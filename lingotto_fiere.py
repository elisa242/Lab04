from Espositore import Espositore
from StandStandard import StandStandard
from StandPreminum import StandPremium
from StandPreseExtra import StandPreseExtra

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self.stand = []
        self.espositori = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        with open(file_path, "r", encoding="utf-8") as f:
            righe = f.readlines()

        for riga in righe:
            riga = riga.strip()
            if riga == "":
                continue

            campi = riga.split(",")
            codice = campi[0]


            if codice.startswith("ES") or len(campi) == 3:
                nome = campi[1]
                cognome = campi[2]
                espositore = Espositore(codice, nome, cognome)
                self.espositori.append(espositore)


            elif codice.startswith("ST"):
                superficie = float(campi[1])
                padiglione = int(campi[2])
                prezzo_base = float(campi[3])

                if len(campi) == 4:
                    # Stand Standard
                    nuovo_stand = StandStandard(
                        codice, superficie, padiglione, prezzo_base
                    )
                elif len(campi) == 5:
                    valore_extra = campi[4]
                    if valore_extra.isdigit():
                        # Stand con Prese Extra
                        numero_prese = int(valore_extra)
                        nuovo_stand = StandPreseExtra(
                            codice, superficie, padiglione, prezzo_base, numero_prese
                        )
                    else:
                        # Stand Premium
                        posizione = valore_extra
                        nuovo_stand = StandPremium(
                            codice, superficie, padiglione, prezzo_base, posizione
                        )
                    self.stand.append(nuovo_stand)

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        stand_trovato = None
        for s in self.stand:
            if s.codice == codice_stand:
                stand_trovato = s
                break

        # Cerchiamo l'espositore
        espositore_trovato = None
        for e in self.espositori:
            if e.codice == codice_espositore:
                espositore_trovato = e
                break


        if stand_trovato is None or espositore_trovato is None:
            raise Exception("Stand o espositore non trovati.")


        if stand_trovato.espositore_assegnato is not None:
            raise Exception("Questo stand è già occupato.")

        stand_trovato.espositore_assegnato = espositore_trovato

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        for e in self.espositori:
            stand_trovato = None
            for s in self.stand:
                if s.espositore_assegnato == e:
                    stand_trovato = s
                    break


            if stand_trovato is not None:
                print(f"L'espositore {e.codice} ha lo stand {stand_trovato.codice}")
            else:
                print(f"L'espositore {e.codice} non ha alcuno stand")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        return sorted(self.stand)
