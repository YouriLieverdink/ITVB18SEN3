import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.mlab as mlab


def draw_graph(data):
    # OPGAVE 1
    # Maak een scatter-plot van de data die als parameter aan deze functie wordt meegegeven. Deze data
    # is een twee-dimensionale matrix met in de eerste kolom de grootte van de steden, in de tweede
    # kolom de winst van de vervoerder. Zet de eerste kolom op de x-as en de tweede kolom op de y-as.
    # Je kunt hier gebruik maken van de mogelijkheid die Python biedt om direct een waarde toe te kennen
    # aan meerdere variabelen, zoals in het onderstaande voorbeeld:

    #     l = [ 3, 4 ]
    #     x,y = l      ->  x = 3, y = 4

    # Om deze constructie in dit specifieke geval te kunnen gebruiken, moet de data-matrix wel eerst
    # roteren (waarom?).
    # Maak gebruik van pytplot.scatter om dit voor elkaar te krijgen.

    # YOUR CODE HERE
    for l in data:
        x, y = l
        plt.scatter(x, y)

    plt.show()


def compute_cost(X, y, theta):
    # OPGAVE 2
    # Deze methode berekent de kosten van de huidige waarden van theta, dat wil zeggen de mate waarin de
    # voorspelling (gegeven de specifieke waarde van theta) correspondeert met de werkelijke waarde (die
    # is gegeven in y).

    # Elk datapunt in X wordt hierin vermenigvuldigd met theta (welke dimensies hebben X en dus theta?)
    # en het resultaat daarvan wordt vergeleken met de werkelijke waarde (dus met y). Het verschil tussen
    # deze twee waarden wordt gekwadrateerd en het totaal van al deze kwadraten wordt gedeeld door het
    # aantal data-punten om het gemiddelde te krijgen. Dit gemiddelde moet je retourneren (de variabele
    # J: een getal, kortom).

    # Een stappenplan zou het volgende kunnen zijn:

    #    1. bepaal het aantal datapunten
    #    2. bepaal de voorspelling (dus elk punt van X maal de huidige waarden van theta)
    #    3. bereken het verschil tussen deze voorspelling en de werkelijke waarde
    #    4. kwadrateer dit verschil
    #    5. tal al deze kwadraten bij elkaar op en deel dit door twee keer het aantal datapunten

    J = 0

    """
        1.
        Het attribuut 'shape' bevat de dimensies van een matrix. De eerste waarde die je terugkrijgt 
        is het aantal rijen en de tweede waarde het aantal kolommen binnen een rij. Dit komt dus
        overeen met het aantal datapunten (m) en het aantal features (n).
    """
    m, n = X.shape

    """
        2.
        De 'dot' functie vermenigvuldigt de gegeven matrix met een vector. Om deze functie correct
        te laten werken moet ervoor worden gezord dat de (n) van beide overeenkomt. Dit wordt
        gedaan door een 1 toe te voegen aan de datapunten (X).

        X = [
            [ 1.    6.1101]
            [ 1.    5.5277]
        ]
        -> Nu is het aantal kolommen gelijk aan 2.

        theta = [
            [ 0. ]
            [ 0. ]
        ]
        -> Hier is het aantal rijen gelijk aan 2.

        Omdat deze beide waarden gelijk aan elkaar zijn kunnen ze worden gevermenigvuldigd.
    """
    h = np.dot(X, theta)

    """
        3.
        Hier worden de actuele waarden van de voorspelde waarden afgetrokken. Wanneer deze syntax
        wordt gebruikt op twee matrixen (A - B) wordt er voor elk element in de eerste, het element
        op dezelfde locatie in de tweede afgetrokken. (A[i] - B[i])

        4.
        Hetzelfde geldt voor het kwadrateren. Elke waarde in de matrix wordt op zichzelf 
        gekwadrateert. Dit wordt gedaan zodat de grootste fouten het duidelijkst worden opgemerkt.
    """
    delta = (h - y) ** 2

    """
        5.
        De verschillen worden bij elkaar opgeteld en vervolgens wordt dat gedeel door het aantal
        datapunten * 2. Zo wordt de 'gemiddelde' fout berekent wat uiteindelijk de kosten is van de
        ontvangen theta.
    """
    J = sum(delta) / (m * 2)

    return J


def gradient_descent(X, y, theta, alpha, num_iters):
    # OPGAVE 3a
    # In deze opgave wordt elke parameter van theta num_iter keer geüpdate om de optimale waarden
    # voor deze parameters te vinden. Per iteratie moet je alle parameters van theta update.

    # Elke parameter van theta wordt verminderd met de som van de fout van alle datapunten
    # vermenigvuldigd met het datapunt zelf (zie Blackboard voor de formule die hierbij hoort).
    # Deze som zelf wordt nog vermenigvuldigd met de 'learning rate' alpha.

    # Een mogelijk stappenplan zou zijn:
    #
    # Voor elke iteratie van 1 tot num_iters:
    #   1. bepaal de voorspelling voor het datapunt, gegeven de huidige waarde van theta
    #   2. bepaal het verschil tussen deze voorspelling en de werkelijke waarde
    #   3. vermenigvuldig dit verschil met de i-de waarde van X
    #   4. update de i-de parameter van theta, namelijk door deze te verminderen met
    #      alpha keer het gemiddelde van de som van de vermenigvuldiging uit 3

    m, n = X.shape
    costs = []

    """
        0. Door middel van deze loop geven we simpelweg aan hoevaak we theta zouden willen
        verbeteren.
    """
    for _ in range(num_iters):

        """
            1. We bepalen hier de voorspelling op dezelfde manier als in de 'compute_cost' functie
            die hierboven staat. Echter moeten we hier wel de theta roteren.

            We krijgen de theta als volgt binnen: 

            theta = [
                [0. 0.]
            ]

            en we willen hem graag zo:

            theta = [
                [0.]
                [0.]
            ]

            omdat het aantal rijen dan weer overeenkomt met het aantal kolommen in X. Als we dit 
            niet zouden doen kunnen we de 'dot' functie niet gebruiken.
        """
        h = np.dot(X, theta.T)

        """
            2. Vervolgens berekenen we het verschil tussen de voorspelde waarde en de actuele waarde
            net zoals in de 'compute_cost' functie.

            Merk op dat we hier vervolgens niet het verschil kwadrateren. Dit is het resultaat van
            het partieel differentieren van de 'kosten' functie.
        """
        delta = h - y

        """
            3. Daarna vermenigvuldigen we dit verschil met de waarden uit X.

            Ook dit is het resultaat van het partieel differtieren van de 'kosten' functie.
        """
        result = delta * X

        """
            4. Om vervolgens de nieuwe waarde van theta te berekenen moeten we een aantal stappen
            uitvoeren. Zo worden alle resultaten bij elkaar opgeteld tot één totaal. Vervolgens
            wordt dit door het aantal punten gedeeld om een gemiddelde te krijgen.

            De 'alpha' in de onderstaande regel code wordt ook wel de 'learning rate' genoemd. Deze
            waarde geeft aan hoe 'snel' het programma de waarde van theta moet aanpassen.
        """
        theta -= alpha * (sum(result) / m)

        costs.append(compute_cost(X, y, theta.T))

    # aan het eind van deze loop retourneren we de nieuwe waarde van theta
    # (wat is de dimensionaliteit van theta op dit moment?).

    return theta, costs


def draw_costs(data):
    # OPGAVE 3b
    plt.plot(data)
    plt.show()


def contour_plot(X, y):
    # OPGAVE 4
    # Deze methode tekent een contour plot voor verschillende waarden van theta_0 en theta_1.
    # De infrastructuur en algemene opzet is al gegeven; het enige wat je hoeft te doen is
    # de matrix J_vals vullen met waarden die je berekent aan de hand van de methode computeCost,
    # die je hierboven hebt gemaakt.
    # Je moet hiervoor door de waarden van t1 en t2 itereren, en deze waarden in een ndarray
    # zetten. Deze ndarray kun je vervolgens meesturen aan de functie computeCost. Bedenk of je nog een
    # transformatie moet toepassen of niet. Let op: je moet computeCost zelf *niet* aanpassen.

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    jet = plt.get_cmap('jet')

    t1 = np.linspace(-10, 10, 100)
    t2 = np.linspace(-1, 4, 100)
    T1, T2 = np.meshgrid(t1, t2)

    J_vals = np.zeros((len(t2), len(t2)))

    """
        t1 en t2 kunnen worden gebruikt voor het creeën van de verschillende startwaarden van theta.
        In het hoorcollege is laten zien dat sommige startwaarden een andere hypothese oplevert.
        Door een groot aantal te 'proberen' is de kans groter dat je een absoluut minimum krijgt
        over een lokaal minimum.
    """
    for i, theta0 in enumerate(t1):
        for j, theta1 in enumerate(t2):
            # Hier maken we de waarde van theta door ze te combineren.
            theta = np.array([theta0, theta1])
            # Vervolgens berekenen we de kosten en zetten deze in de 'J_vals'.
            J = compute_cost(X, y, theta)
            J_vals[i][j] = J[0]

    surf = ax.plot_surface(T1, T2, J_vals, rstride=1, cstride=1,
                           cmap=cm.coolwarm, linewidth=0, antialiased=False)

    xLabel = ax.set_xlabel(r'$\theta_0$', linespacing=3.2)
    yLabel = ax.set_ylabel(r'$\theta_1$', linespacing=3.1)
    zLabel = ax.set_zlabel(r'$J(\theta_0, \theta_1)$', linespacing=3.4)

    ax.dist = 10

    plt.show()
