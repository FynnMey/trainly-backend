import os
from models.user import User
from models.exercise import Exercise
from extensions import db
from dotenv import load_dotenv

load_dotenv()

def seed_data():
    if not User.query.first():
        admin = User(
            id=0,
            name=os.getenv("ACCOUNT_NAME"),
            account=os.getenv("ACCOUNT"),
            password_hash=os.getenv("ACCOUNT_HASP_PASSWORD")
        )
        db.session.add(admin)
        db.session.commit()

    if not Exercise.query.first():
        exercises = [
            Exercise(
                name="Beinpresse",
                description="Die Beine werden im Sitzen gegen eine Plattform gedrückt. Trainiert primär Oberschenkel und Gesäß.",
                image_url="/static/exercise/images/beinpresse.png",
                gif_url="/static/exercise/gifs/beinpresse.gif",
                muscle_groups=["Quadrizeps", "Gesäßmuskulatur", "Beinbeuger"]
            ),

            Exercise(
                name="Beinstrecker",
                description="Im Sitzen werden die Beine gegen ein Polster nach oben gestreckt. Isoliertes Training des Quadrizeps.",
                image_url="/static/exercise/images/beinstrecker.png",
                gif_url="/static/exercise/gifs/beinstrecker.gif",
                muscle_groups=["Quadrizeps"]
            ),

            Exercise(
                name="Beinbeuger sitzend",
                description="Im Sitzen werden die Unterschenkel gegen ein Polster nach hinten gezogen. Effektives Training der Beinbeuger.",
                image_url="/static/exercise/images/beinbeuger_sitzend.png",
                gif_url="/static/exercise/gifs/beinbeuger_sitzend.gif",
                muscle_groups=["Beinbeuger", "Gesäßmuskulatur"]
            ),

            Exercise(
                name="Beinbeuger liegend",
                description="In Bauchlage werden die Beine gegen ein Polster nach oben gezogen. Fokus liegt auf der hinteren Oberschenkelmuskulatur.",
                image_url="/static/exercise/images/beinbeuger_liegend.png",
                gif_url="/static/exercise/gifs/beinbeuger_liegend.webp",
                muscle_groups=["Beinbeuger"]
            ),

            Exercise(
                name="Adduktorenmaschine",
                description="Im Sitzen werden die Beine kontrolliert nach innen geführt. Trainiert die Oberschenkelinnenseite.",
                image_url="/static/exercise/images/adduktorenmaschine.png",
                gif_url="/static/exercise/gifs/adduktorenmaschine.webp",
                muscle_groups=["Adduktoren"]
            ),

            Exercise(
                name="Abduktorenmaschine",
                description="Die Beine werden im Sitzen nach außen gedrückt. Zielt auf die äußere Oberschenkelmuskulatur und das Gesäß.",
                image_url="/static/exercise/images/abduktorenmaschine.png",
                gif_url="/static/exercise/gifs/abduktorenmaschine.webp",
                muscle_groups=["Abduktoren", "Gesäßmuskulatur"]
            ),

            Exercise(
                name="Wadenheben sitzend",
                description="Im Sitzen werden die Fersen angehoben, um die Wadenmuskulatur zu trainieren.",
                image_url="/static/exercise/images/wadenheben_sitzend.png",
                gif_url="/static/exercise/gifs/wadenheben_sitzend.webp",
                muscle_groups=["Waden"]
            ),

            Exercise(
                name="Wadenheben stehend (Maschine)",
                description="Im Stehen wird der Körper durch Streckung der Fußgelenke angehoben. Aktiviert besonders die Waden.",
                image_url="/static/exercise/images/wadenheben_stehend.png",
                gif_url="/static/exercise/gifs/wadenheben_stehend.webp",
                muscle_groups=["Waden"]
            ),
            Exercise(
                name="Glute Kickback (Kabel oder Maschine)",
                description="Im Vierfüßlerstand oder an der Maschine wird ein Bein nach hinten oben gestreckt, um gezielt den Gluteus Maximus zu aktivieren.",
                image_url="/static/exercise/images/glute_kickback.png",
                gif_url="/static/exercise/gifs/glute_kickback.gif",
                muscle_groups=["Gesäßmuskulatur", "Beinbeuger"]
            ),

            Exercise(
                name="Hip Thrust Maschine",
                description="Der Rücken liegt stabil an einem Polster, das Becken wird gegen Widerstand nach oben gedrückt. Fokus auf Gesäßmuskulatur.",
                image_url="/static/exercise/images/hip_thrust_maschine.png",
                gif_url="/static/exercise/gifs/hip_thrust_maschine.webp",
                muscle_groups=["Gesäßmuskulatur", "Beinbeuger"]
            ),

            Exercise(
                name="Stepper (Kardio & Beine)",
                description="Simuliert das Treppensteigen mit gleichmäßigem Widerstand. Stärkt vor allem Oberschenkel und Po.",
                image_url="/static/exercise/images/stepper.png",
                gif_url="/static/exercise/gifs/stepper.webp",
                muscle_groups=["Quadrizeps", "Gesäßmuskulatur", "Waden"]
            ),

            Exercise(
                name="Hackenschmidt Maschine (Hack Squat)",
                description="Geführte Kniebeuge in schräger Position. Ideal für kontrolliertes Beintraining mit Fokus auf Oberschenkel.",
                image_url="/static/exercise/images/hackenschmidt.png",
                gif_url="/static/exercise/gifs/hackenschmidt.webp",
                muscle_groups=["Quadrizeps", "Gesäßmuskulatur", "Beinbeuger"]
            ),

            Exercise(
                name="Multipresse Kniebeuge",
                description="Geführte Kniebeuge mit Langhantel in der Smith Machine. Mehr Stabilität, ideal für kontrolliertes Beintraining.",
                image_url="/static/exercise/images/multipresse_kniebeuge.png",
                gif_url="/static/exercise/gifs/multipresse_kniebeuge.webp",
                muscle_groups=["Quadrizeps", "Gesäßmuskulatur", "Beinbeuger"]
            ),
            Exercise(
                name="Brustpresse (Chest Press)",
                description="Im Sitzen drückst du zwei Griffe kontrolliert nach vorne. Trainiert die gesamte Brustmuskulatur und den Trizeps.",
                image_url="/static/exercise/images/brustpresse.png",
                gif_url="/static/exercise/gifs/brustpresse.webp",
                muscle_groups=["Brust", "Trizeps", "Vordere Schulter"]
            ),

            Exercise(
                name="Butterfly (Pec Deck)",
                description="Mit leicht gebeugten Armen führst du die Griffe vor der Brust zusammen. Isoliertes Training der Brustmuskulatur.",
                image_url="/static/exercise/images/butterfly.png",
                gif_url="/static/exercise/gifs/butterfly.webp",
                muscle_groups=["Brust"]
            ),

            Exercise(
                name="Kabelzug-Fliegende (stehend)",
                description="Mit Griffen im Kabelzug führst du die Arme wie bei Fliegenden zusammen. Fokus auf inneren Brustbereich.",
                image_url="/static/exercise/images/kabel_fliegende.png",
                gif_url="/static/exercise/gifs/kabel_fliegende.gif",
                muscle_groups=["Brust", "Vordere Schulter"]
            ),

            Exercise(
                name="Schrägbank Brustpresse (Maschine)",
                description="Sitzend in leicht zurückgelehnter Position drückst du die Griffe nach vorne oben. Betonung des oberen Brustbereichs.",
                image_url="/static/exercise/images/schraegbank_presse.png",
                gif_url="/static/exercise/gifs/schraegbank_presse.webp",
                muscle_groups=["Brust", "Vordere Schulter", "Trizeps"]
            ),

            Exercise(
                name="Brustpresse liegend (Plate Loaded)",
                description="In Rückenlage drückst du Gewichtsarme mit beiden Händen nach oben. Trainingsfokus liegt auf der mittleren Brust.",
                image_url="/static/exercise/images/brustpresse_liegend.png",
                gif_url="/static/exercise/gifs/brustpresse_liegend.webp",
                muscle_groups=["Brust", "Trizeps"]
            ),
            Exercise(
                name="Latzug zur Brust",
                description="Im Sitzen ziehst du eine breite Stange kontrolliert zur Brust. Ziel ist der breite Rückenmuskel (Latissimus).",
                image_url="/static/exercise/images/latzug_zur_brust.png",
                gif_url="/static/exercise/gifs/latzug_zur_brust.webp",
                muscle_groups=["Latissimus", "Bizeps", "Hintere Schulter"]
            ),

            Exercise(
                name="Latzug hinter den Kopf",
                description="Wie beim klassischen Latzug, aber die Stange wird hinter den Kopf gezogen. Nur für Fortgeschrittene empfohlen.",
                image_url="/static/exercise/images/latzug_hinter_kopf.png",
                gif_url="/static/exercise/gifs/latzug_hinter_kopf.gif",
                muscle_groups=["Latissimus", "Trapezmuskel"]
            ),

            Exercise(
                name="Rudermaschine (sitzend, eng)",
                description="Ziehgriff wird eng zur Körpermitte geführt. Stärkt Rückenmitte und Bizeps.",
                image_url="/static/exercise/images/rudermaschine_eng.png",
                gif_url="/static/exercise/gifs/rudermaschine_eng.webp",
                muscle_groups=["Rücken", "Bizeps"]
            ),

            Exercise(
                name="Rudermaschine (breit)",
                description="Mit breitem Griff ruderst du zur Brust. Ziel ist die obere Rückenmuskulatur.",
                image_url="/static/exercise/images/rudermaschine_breit.png",
                gif_url="/static/exercise/gifs/rudermaschine_breit.webp",
                muscle_groups=["Rücken", "Hintere Schulter", "Latissimus"]
            ),

            Exercise(
                name="Rückenstrecker (Hyperextension)",
                description="Im Sitzen oder auf einer Bank wird der Oberkörper kontrolliert nach oben gestreckt. Stärkt unteren Rücken.",
                image_url="/static/exercise/images/rueckenstrecker.png",
                gif_url="/static/exercise/gifs/rueckenstrecker.webp",
                muscle_groups=["Unterer Rücken", "Gesäßmuskulatur"]
            ),

            Exercise(
                name="Reverse Butterfly",
                description="Arme werden nach hinten geführt. Trainiert den oberen Rücken und die hintere Schulter.",
                image_url="/static/exercise/images/reverse_butterfly.png",
                gif_url="/static/exercise/gifs/reverse_butterfly.webp",
                muscle_groups=["Hintere Schulter", "Trapezmuskel", "Rücken"]
            ),

            Exercise(
                name="Kabelrudern (Kabelzug, sitzend)",
                description="Mit einem V-Griff oder Seil wird die Zugbewegung zur Körpermitte ausgeführt. Effektives Rücken- und Armtraining.",
                image_url="/static/exercise/images/kabelrudern.png",
                gif_url="/static/exercise/gifs/kabelrudern.webp",
                muscle_groups=["Latissimus", "Rücken", "Bizeps"]
            ),
            Exercise(
                name="Schulterpresse (Maschine)",
                description="Im Sitzen drückst du die Griffe über den Kopf. Fokus auf die vordere und mittlere Schultermuskulatur.",
                image_url="/static/exercise/images/schulterpresse.png",
                gif_url="/static/exercise/gifs/schulterpresse.webp",
                muscle_groups=["Schultern", "Trizeps"]
            ),

            Exercise(
                name="Seitheben Maschine",
                description="Seitliches Anheben der Arme gegen Widerstand. Ideal zur Isolation des mittleren Deltamuskels.",
                image_url="/static/exercise/images/seitheben_maschine.png",
                gif_url="/static/exercise/gifs/seitheben_maschine.webp",
                muscle_groups=["Schultern"]
            ),

            Exercise(
                name="Frontheben Kabelzug",
                description="Mit geradem Arm den Griff vor dem Körper anheben. Fokus auf die vordere Schulter.",
                image_url="/static/exercise/images/frontheben_kabel.png",
                gif_url="/static/exercise/gifs/frontheben_kabel.webp",
                muscle_groups=["Vordere Schulter"]
            ),

            Exercise(
                name="Face Pulls (Kabelzug)",
                description="Mit Seil auf Augenhöhe ziehen, Ellenbogen nach außen. Stärkt hintere Schulter und Haltungsmuskeln.",
                image_url="/static/exercise/images/face_pulls.png",
                gif_url="/static/exercise/gifs/face_pulls.webp",
                muscle_groups=["Hintere Schulter", "Trapezmuskel", "Rotatorenmanschette"]
            ),

            Exercise(
                name="Aufrechtes Rudern (Kabel)",
                description="Vertikale Zugbewegung mit engem Griff bis zur Brust. Belastet den Trapezmuskel und die Schultern.",
                image_url="/static/exercise/images/aufrechtes_rudern.png",
                gif_url="/static/exercise/gifs/aufrechtes_rudern.webp",
                muscle_groups=["Schultern", "Trapezmuskel"]
            ),
            Exercise(
                name="Bizepscurls Maschine",
                description="Im Sitzen beugst du die Arme gegen Widerstand. Isoliertes Training des Bizeps.",
                image_url="/static/exercise/images/bizepscurls_maschine.png",
                gif_url="/static/exercise/gifs/bizepscurls_maschine.webp",
                muscle_groups=["Bizeps"]
            ),

            Exercise(
                name="Bizepscurls Kabelzug",
                description="Mit geradem oder SZ-Griff wird der Kabelzug aus dem Stand nach oben gebeugt. Gutes Pumpgefühl.",
                image_url="/static/exercise/images/bizepscurls_kabel.png",
                gif_url="/static/exercise/gifs/bizepscurls_kabel.webp",
                muscle_groups=["Bizeps"]
            ),

            Exercise(
                name="Konzentrationscurls (Kabel)",
                description="Mit einem Arm wird der Griff aus tiefer Position langsam nach oben geführt. Isolation pur.",
                image_url="/static/exercise/images/konzentrationscurls_kabel.png",
                gif_url="/static/exercise/gifs/konzentrationscurls_kabel.webp",
                muscle_groups=["Bizeps"]
            ),

            Exercise(
                name="Trizepsdrücken Seilzug",
                description="Mit einem Seil ziehst du die Arme kontrolliert nach unten. Fokus auf die Trizepsköpfe.",
                image_url="/static/exercise/images/trizepsdruecken_seil.png",
                gif_url="/static/exercise/gifs/trizepsdruecken_seil.webp",
                muscle_groups=["Trizeps"]
            ),

            Exercise(
                name="Trizepsdrücken SZ-Griff",
                description="Ähnlich wie beim Seil, aber mit starrer SZ-Stange. Etwas mehr Fokus auf den langen Trizepskopf.",
                image_url="/static/exercise/images/trizepsdruecken_sz.png",
                gif_url="/static/exercise/gifs/trizepsdruecken_sz.webp",
                muscle_groups=["Trizeps"]
            ),

            Exercise(
                name="Trizepsmaschine (Dips)",
                description="Im Sitzen drückst du die Griffe nach unten/hinten. Effektiv für den gesamten Trizeps.",
                image_url="/static/exercise/images/trizepsmaschine.png",
                gif_url="/static/exercise/gifs/trizepsmaschine.webp",
                muscle_groups=["Trizeps"]
            ),
            Exercise(
                name="Crunchmaschine (Bauchpresse)",
                description="Im Sitzen ziehst du Oberkörper und Beine zusammen gegen Widerstand. Fokus auf den geraden Bauchmuskel.",
                image_url="/static/exercise/images/crunchmaschine.png",
                gif_url="/static/exercise/gifs/crunchmaschine.webp",
                muscle_groups=["Gerader Bauchmuskel"]
            ),

            Exercise(
                name="Kabel-Crunch (knieend)",
                description="Mit einem Seil ziehst du aus dem Kniestand den Oberkörper nach unten. Sehr effektive Spannung auf dem Bauch.",
                image_url="/static/exercise/images/kabel_crunch.png",
                gif_url="/static/exercise/gifs/kabel_crunch.webp",
                muscle_groups=["Gerader Bauchmuskel"]
            ),

            Exercise(
                name="Beinheben hängend",
                description="Im Hang hebst du deine gestreckten oder gebeugten Beine an. Aktiviert unteren Bauch und Hüftbeuger.",
                image_url="/static/exercise/images/beinheben_haengend.png",
                gif_url="/static/exercise/gifs/beinheben_haengend.webp",
                muscle_groups=["Unterer Bauch", "Hüftbeuger"]
            ),

            Exercise(
                name="Beinheben auf Rückenstreckerbank",
                description="Auf der Schrägbank werden die Beine oder Knie angezogen. Fokus auf unteren Bauchbereich.",
                image_url="/static/exercise/images/beinheben_bank.png",
                gif_url="/static/exercise/gifs/beinheben_bank.webp",
                muscle_groups=["Unterer Bauch"]
            ),

            Exercise(
                name="Rumpfdrehen Maschine",
                description="Im Sitzen drehst du den Oberkörper gegen Widerstand. Trainiert die seitlichen Bauchmuskeln (Schrägen).",
                image_url="/static/exercise/images/rumpfdrehen_maschine.png",
                gif_url="/static/exercise/gifs/rumpfdrehen_maschine.webp",
                muscle_groups=["Schräge Bauchmuskeln"]
            ),

            Exercise(
                name="Seitbeugen mit Kurzhantel (Alternativübung)",
                description="Im Stand neigst du den Oberkörper zur Seite mit einer Hantel. Ziel sind die schrägen Bauchmuskeln.",
                image_url="/static/exercise/images/seitbeugen.png",
                gif_url="/static/exercise/gifs/seitbeugen.webp",
                muscle_groups=["Schräge Bauchmuskeln"]
            ),
            Exercise(
                name="Kniebeuge (frei)",
                description="Die klassische Kniebeuge mit dem eigenen Körpergewicht oder mit Langhantel. Effektives Ganzkörpertraining mit Fokus auf die Beine und das Gesäß.",
                image_url="/static/exercise/images/kniebeuge_frei.png",
                gif_url="/static/exercise/gifs/kniebeuge_frei.gif",
                muscle_groups=["Quadrizeps", "Gesäßmuskulatur", "Beinbeuger", "Rumpf"]
            ),

            Exercise(
                name="Kreuzheben (Langhantel)",
                description="Mit geradem Rücken wird die Langhantel vom Boden angehoben. Beansprucht Rücken, Beine und Gesäß.",
                image_url="/static/exercise/images/kreuzheben.png",
                gif_url="/static/exercise/gifs/kreuzheben.webp",
                muscle_groups=["Rücken", "Beinbeuger", "Gesäßmuskulatur", "Rumpf"]
            ),

            Exercise(
                name="Bankdrücken (Langhantel)",
                description="Im Liegen wird die Langhantel von der Brust nach oben gedrückt. Klassiker für den Brustaufbau.",
                image_url="/static/exercise/images/bankdruecken.png",
                gif_url="/static/exercise/gifs/bankdruecken.webp",
                muscle_groups=["Brust", "Trizeps", "Vordere Schulter"]
            ),

            Exercise(
                name="Kurzhantel Fliegende",
                description="Auf einer Flachbank führst du mit zwei Kurzhanteln eine breite Bewegung aus. Zielt auf die Brustmuskeln.",
                image_url="/static/exercise/images/kurzhantel_fliegende.png",
                gif_url="/static/exercise/gifs/kurzhantel_fliegende.webp",
                muscle_groups=["Brust", "Vordere Schulter"]
            ),

            Exercise(
                name="Kurzhantelrudern (einarmig)",
                description="Einarmiges Rudern auf der Flachbank. Effektiv für Latissimus und Rückenmitte.",
                image_url="/static/exercise/images/kurzhantelrudern.png",
                gif_url="/static/exercise/gifs/kurzhantelrudern.webp",
                muscle_groups=["Rücken", "Latissimus", "Bizeps"]
            ),

            Exercise(
                name="Arnold Press",
                description="Variation der Schulterpresse mit Kurzhanteln, bei der du mit einer Drehung arbeitest. Beansprucht mehrere Schultermuskeln.",
                image_url="/static/exercise/images/arnold_press.png",
                gif_url="/static/exercise/gifs/arnold_press.webp",
                muscle_groups=["Schultern", "Trizeps"]
            ),

            Exercise(
                name="Plank (Unterarmstütz)",
                description="Statisch gehaltene Position auf den Unterarmen. Stärkt die gesamte Rumpfmuskulatur.",
                image_url="/static/exercise/images/plank.png",
                gif_url="/static/exercise/gifs/plank.png",
                muscle_groups=["Bauch", "Rumpf", "Schultern"]
            ),

            Exercise(
                name="Mountain Climbers",
                description="Im Liegestütz werden die Beine abwechselnd nach vorne gezogen. Ideal für Bauch und Ausdauer.",
                image_url="/static/exercise/images/mountain_climbers.png",
                gif_url="/static/exercise/gifs/mountain_climbers.webp",
                muscle_groups=["Bauch", "Beine", "Kardiovaskular"]
            ),

            Exercise(
                name="Klimmzug (frei)",
                description="Aus dem Hang wird das Kinn über die Stange gezogen. Klassiker für Rücken und Arme.",
                image_url="/static/exercise/images/klimmzug.png",
                gif_url="/static/exercise/gifs/klimmzug.webp",
                muscle_groups=["Latissimus", "Bizeps", "Rücken", "Schultern"]
            ),
            Exercise(
                name="Liegestütze",
                description="Mit geradem Körper drückst du dich aus der Bauchlage vom Boden ab. Trainiert Brust, Schultern und Trizeps.",
                image_url="/static/exercise/images/liegestuetze.png",
                gif_url="/static/exercise/gifs/liegestuetze.webp",
                muscle_groups=["Brust", "Trizeps", "Vordere Schulter", "Rumpf"]
            ),

            Exercise(
                name="Squats (Kniebeugen)",
                description="Mit dem eigenen Körpergewicht gehst du in die Hocke und wieder hoch. Einfach und effektiv für Beine und Gesäß.",
                image_url="/static/exercise/images/squats.png",
                gif_url="/static/exercise/gifs/squats.gif",
                muscle_groups=["Quadrizeps", "Gesäßmuskulatur", "Beinbeuger"]
            ),

            Exercise(
                name="Ausfallschritte (Lunges)",
                description="Abwechselnd einen Schritt nach vorne machen und tief gehen. Effektives Bein- und Gesäßtraining.",
                image_url="/static/exercise/images/ausfallschritte.png",
                gif_url="/static/exercise/gifs/ausfallschritte.webp",
                muscle_groups=["Quadrizeps", "Gesäßmuskulatur", "Beinbeuger", "Rumpf"]
            ),

            Exercise(
                name="Wandsitzen",
                description="An eine Wand lehnen, in der Hocke halten. Statische Übung für Oberschenkel und Ausdauer.",
                image_url="/static/exercise/images/wandsitzen.png",
                gif_url="/static/exercise/gifs/wandsitzen.webp",
                muscle_groups=["Quadrizeps", "Gesäßmuskulatur"]
            ),

            Exercise(
                name="Superman",
                description="Flach auf dem Bauch liegend Arme und Beine gleichzeitig anheben. Stärkt unteren Rücken.",
                image_url="/static/exercise/images/superman.png",
                gif_url="/static/exercise/gifs/superman.webp",
                muscle_groups=["Unterer Rücken", "Gesäßmuskulatur", "Schultern"]
            ),

            Exercise(
                name="Seitstütz (Side Plank)",
                description="Seitlich auf dem Unterarm gestützt den Körper stabil halten. Ziel ist der seitliche Bauch.",
                image_url="/static/exercise/images/seitstuetz.png",
                gif_url="/static/exercise/gifs/seitstuetz.webp",
                muscle_groups=["Schräge Bauchmuskeln", "Rumpf", "Schultern"]
            ),

            Exercise(
                name="Glute Bridge",
                description="Rückenlage, Füße aufgestellt, Hüfte nach oben drücken. Aktiviert Gesäß und unteren Rücken.",
                image_url="/static/exercise/images/glute_bridge.png",
                gif_url="/static/exercise/gifs/glute_bridge.webp",
                muscle_groups=["Gesäßmuskulatur", "Beinbeuger", "Rumpf"]
            ),

            Exercise(
                name="Bergsteiger (Mountain Climbers)",
                description="Aus der Plank-Position Beine abwechselnd nach vorne ziehen. Ideal für Bauch und Ausdauer.",
                image_url="/static/exercise/images/bergsteiger.png",
                gif_url="/static/exercise/gifs/bergsteiger.webp",
                muscle_groups=["Bauch", "Beine", "Kardiovaskular"]
            ),

            Exercise(
                name="Russian Twists",
                description="Im Sitzen leicht zurücklehnen und Oberkörper abwechselnd nach links und rechts drehen. Stärkt schräge Bauchmuskeln.",
                image_url="/static/exercise/images/russian_twists.png",
                gif_url="/static/exercise/gifs/russian_twists.webp",
                muscle_groups=["Schräge Bauchmuskeln", "Rumpf"]
            ),

            Exercise(
                name="Fahrrad-Crunches",
                description="Im Liegen mit den Beinen in Pedalbewegung, dabei Ellenbogen zum gegenüberliegenden Knie führen.",
                image_url="/static/exercise/images/fahrrad_crunches.png",
                gif_url="/static/exercise/gifs/fahrrad_crunches.webp",
                muscle_groups=["Bauch", "Schräge Bauchmuskeln"]
            ),

            Exercise(
                name="Donkey Kicks",
                description="Im Vierfüßlerstand wird ein Bein nach oben und hinten gedrückt. Effektiv für Gesäß und Beinbeuger.",
                image_url="/static/exercise/images/donkey_kicks.png",
                gif_url="/static/exercise/gifs/donkey_kicks.webp",
                muscle_groups=["Gesäßmuskulatur", "Beinbeuger"]
            ),
            Exercise(
                name="Glute Isolator",
                description="Im Stehen wird ein Bein nach hinten gegen Widerstand gedrückt. Isoliertes Training des Gluteus Maximus.",
                image_url="/static/exercise/images/glute_isolator.png",
                gif_url="/static/exercise/gifs/glute_isolator.webp",
                muscle_groups=["Gesäßmuskulatur", "Beinbeuger"]
            ),

            Exercise(
                name="T-Bar Rudern Maschine",
                description="Mit Brustauflage wird ein Griff zur Körpermitte gezogen. Effektiv für mittleren Rücken und Latissimus.",
                image_url="/static/exercise/images/tbar_rudern.png",
                gif_url="/static/exercise/gifs/tbar_rudern.webp",
                muscle_groups=["Rücken", "Latissimus", "Bizeps"]
            ),

            Exercise(
                name="Shrug Maschine",
                description="Die Schultern werden nach oben gezogen, um den Nacken gezielt zu trainieren.",
                image_url="/static/exercise/images/shrug_maschine.png",
                gif_url="/static/exercise/gifs/shrug_maschine.webp",
                muscle_groups=["Trapezmuskel"]
            ),

            Exercise(
                name="Cable Crossover (Crossover Station)",
                description="Mit zwei Kabelzügen werden kontrollierte Bewegungen ausgeführt. Vielseitig für Brust, Arme und Schultern.",
                image_url="/static/exercise/images/cable_crossover.png",
                gif_url="/static/exercise/gifs/cable_crossover.webp",
                muscle_groups=["Brust", "Vordere Schulter", "Trizeps"]
            ),

        ]

        db.session.add_all(exercises)
        db.session.commit()
