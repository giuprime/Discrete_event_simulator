# discrete_event_simulator
# Author: Giuseppe Primerano
# Created: 08/10/2023
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Questo progetto riguarda la realizzazione di un simulatore di eventi discreti. Il progetto si basa sull'analisi di una coda di tipo M/M/1 quindi è caratterizzata dalla presenza di un solo server 
e di un numero di clienti infinito.
Il progetto utilizza Python e un approccio OOP.
Gli arrivi dei clienti e il loro tempo di servizio sono generati casualmente seguendo la funzione esponenziale e un arrival_rate e service_rate inseriti manualmente dall'utente.
Venogno calcolati diversi valori tra cui la lunghezza della coda, il tempo medio di attesa ecc.
I risultati dei cacloli sono inseriti all'interno di un file .xlxs per la loro analisi.

This project is a discrete event simulator. Simulate a M/M/1 queue in which we've only one server but the number of customer is infinite.
This project was create dwith Python and an OOP approach.
The arrival and service rate of the costumer are distributed according with an Exponential distribution, the arrival and service rate are input.
At the end of the simulation there's the calculation of different values like the expected queue lenght, the average wait time, the average service time etc.
The results are sended to an .xlxs file for the calculation.
