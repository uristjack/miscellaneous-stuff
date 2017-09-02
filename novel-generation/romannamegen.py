import random

def romannamemale():
    """Creates a random male Roman name."""
    
    praenomenlist_male = ["Gaius", "Lucius", "Marcus", "Publius", "Quintus",
                          "Titus", "Tiberius", "Sextus", "Aulus", "Decimus",
                          "Gnaeus", "Spurius", "Manius", "Servius", "Appius",
                          "Numerius", "Vibius"]    

    nomenlist = ["Acilius", "Aebutius", "Aelius", "Aemilius", "Albius", "Amatius", "Annaeus", "Anneius",
                 "Annius", "Antonius", "Arrius", "Artorius", "Asinius", "Atilius", "Atius", "Aurelius",
                 "Autronius", "Caecilius", "Caedicius", "Caelius", "Calidius", "Calpurnius", "Cassius", "Claudius",
                 "Cloelius", "Cocceius", "Cominius", "Cornelius", "Coruncanius", "Curiatius", "Curius", "Curtius",
                 "Decius", "Didius", "Domitius", "Duilius", "Durmius", "Equitius", "Fabius", "Fabricius",
                 "Fannius", "Flavius", "Fulvius", "Furius", "Gabinius", "Galerius", "Geganius", "Gellius",
                 "Geminius", "Genucius", "Gratius", "Herrenius", "Hirtius", "Horatius", "Hortensius", "Hostilius",
                 "Iulius", "Iulianus", "Iunius", "Iuventius", "Laelius", "Lartius", "Licinius", "Livius",
                 "Lucilius", "Lucretius", "Manlius", "Marcius", "Marius", "Memmius", "Menenius", "Minicius",
                 "Minius", "Minucius", "Modius", "Mucius", "Naevius", "Nautius", "Numerius", "Numicius",
                 "Octavius", "Ovidius", "Papirius", "Petronius", "Pinarius", "Pompeius", "Pompilius", "Pontius",
                 "Popillius", "Porcius", "Postumius", "Quinctilius", "Quinctius", "Rubellius", "Rufius", "Rutilius",
                 "Sallustius", "Salonius", "Salvius", "Scribonius", "Seius", "Sempronius", "Sentius", "Sergius",
                 "Sertorius", "Servilius", "Sextius", "Sicinius", "Suetonis", "Sulpicius", "Tarpeius", "Tarquitius",
                 "Terentius", "Titinius", "Titurius", "Tuccius", "Tullius", "Ulpius", "Valerius", "Vedius",
                 "Velleius", "Vergilius", "Verginius", "Vibius", "Villius", "Vipsanius", "Vitellius", "Vitruvius",
                 "Volumnius"]    

    cognomenlist_male = ["Aculeo", "Agricola", "Agrippa", "Ahala", "Ahenobarbus", "Albinus", "Albus", "Ambustus",
                         "Annalis", "Aquila", "Aquilinus", "Arvina", "Asellio", "Asina", "Atellus", "Avitus",
                         "Balbus", "Barba", "Barbatus", "Bassus", "Bestia", "Bibaculus", "Bibulus", "Blaesus",
                         "Brocchus", "Brutus", "Bubulcus", "Bucco", "Bulbus", "Buteo", "Caecus", "Caepio",
                         "Calidus", "Calvus", "Camillus", "Caninus", "Canus", "Capito", "Carbo", "Catilina",
                         "Catulus", "Celer", "Celsus", "Cethegus", "Cicurinus", "Cilo", "Cincinnatus", "Cinna",
                         "Cordus", "Cornicen", "Cornutus", "Corvinus", "Corvus", "Cossus", "Costa", "Cotta",
                         "Crassipes", "Crispinus", "Crispus", "Culleo", "Curio", "Cursor", "Curvus", "Dentatus",
                         "Denter", "Dento", "Dives", "Dolabella", "Dorsuo", "Drusus", "Figulus", "Fimbria",
                         "Flaccus", "Flavus", "Florus", "Fronto", "Fullo", "Fusus", "Galeo", "Gemellus",
                         "Glabrio", "Gracchus", "Gurges", "Habitus", "Helva", "Iullus", "Labeo", "Lactuca",
                         "Laenas", "Lanatus", "Laevinus", "Laterensis", "Lentulus", "Lepidus", "Libo", "Licinus",
                         "Longus", "Lucullus", "Lurco", "Macer", "Macula", "Malleolus", "Mamercus", "Marcellus",
                         "Maro", "Merenda", "Mergus", "Merula", "Messalla", "Metellus", "Murena", "Mus",
                         "Musca", "Nasica", "Naso", "Natta", "Nepos", "Nerva", "Niger", "Novellus",
                         "Ocella", "Pacilus", "Paetus", "Pansa", "Papus", "Paterculus", "Paullus", "Pavo",
                         "Pera", "Pictor", "Piso", "Plancus", "Plautus", "Poplicola", "Postumus", "Potitus",
                         "Praeconinus", "Praetextatus", "Priscus", "Proculus", "Publicola", "Pulcher", "Pullus", "Pulvillus",
                         "Purpureo", "Quadratus", "Ralla", "Regillus", "Regulus", "Rufus", "Ruga", "Rullus",
                         "Rutilus", "Salinator", "Saturninus", "Scaeva", "Scaevola", "Scapula", "Scaurus", "Scrofa",
                         "Severus", "Silanus", "Silo", "Silus", "Stolo", "Strabo", "Structus", "Sura",
                         "Taurus", "Triarius", "Trigeminus", "Trio", "Tubero", "Tubertus", "Tubulus", "Tuditanus",
                         "Tullus", "Turdus", "Varro", "Varus", "Vatia", "Verres", "Vespillo", "Vetus",
                         "Vitulus", "Volusus"]

    praenomen = random.choice(praenomenlist_male)
    nomen = random.choice(nomenlist)
    cognomen = random.choice(cognomenlist_male)
    
    return("%s %s %s" % (praenomen, nomen, cognomen))

def romannamefemale():
    """Creates a random female Roman name."""

    praenomenlist_female = ["Gaia", "Lucia", "Marca", "Publia", "Quinta",
                            "Tita", "Tiberia", "Sexta", "Aula", "Decima",
                            "Gnaea", "Spuria", "Mania", "Servia", "Appia",
                            "Numeria", "Vibia"]

    nomenlist = ["Acilius", "Aebutius", "Aelius", "Aemilius", "Albius", "Amatius", "Annaeus", "Anneius",
                 "Annius", "Antonius", "Arrius", "Artorius", "Asinius", "Atilius", "Atius", "Aurelius",
                 "Autronius", "Caecilius", "Caedicius", "Caelius", "Calidius", "Calpurnius", "Cassius", "Claudius",
                 "Cloelius", "Cocceius", "Cominius", "Cornelius", "Coruncanius", "Curiatius", "Curius", "Curtius",
                 "Decius", "Didius", "Domitius", "Duilius", "Durmius", "Equitius", "Fabius", "Fabricius",
                 "Fannius", "Flavius", "Fulvius", "Furius", "Gabinius", "Galerius", "Geganius", "Gellius",
                 "Geminius", "Genucius", "Gratius", "Herrenius", "Hirtius", "Horatius", "Hortensius", "Hostilius",
                 "Iulius", "Iulianus", "Iunius", "Iuventius", "Laelius", "Lartius", "Licinius", "Livius",
                 "Lucilius", "Lucretius", "Manlius", "Marcius", "Marius", "Memmius", "Menenius", "Minicius",
                 "Minius", "Minucius", "Modius", "Mucius", "Naevius", "Nautius", "Numerius", "Numicius",
                 "Octavius", "Ovidius", "Papirius", "Petronius", "Pinarius", "Pompeius", "Pompilius", "Pontius",
                 "Popillius", "Porcius", "Postumius", "Quinctilius", "Quinctius", "Rubellius", "Rufius", "Rutilius",
                 "Sallustius", "Salonius", "Salvius", "Scribonius", "Seius", "Sempronius", "Sentius", "Sergius",
                 "Sertorius", "Servilius", "Sextius", "Sicinius", "Suetonis", "Sulpicius", "Tarpeius", "Tarquitius",
                 "Terentius", "Titinius", "Titurius", "Tuccius", "Tullius", "Ulpius", "Valerius", "Vedius",
                 "Velleius", "Vergilius", "Verginius", "Vibius", "Villius", "Vipsanius", "Vitellius", "Vitruvius",
                 "Volumnius"]

    cognomenlist_female = ["Aculeo", "Agricola", "Agrippa", "Ahala", "Ahenobarba", "Albina", "Alba", "Ambusta",
                           "Annalis", "Aquila", "Aquilina", "Arvina", "Asellio", "Asina", "Atella", "Avita",
                           "Balba", "Barba", "Barbata", "Bassa", "Bestia", "Bibacula", "Bibula", "Blaesa",
                           "Broccha", "Bruta", "Bubulca", "Bucco", "Bulba", "Buteo", "Caeca", "Caepio",
                           "Calida", "Calva", "Camilla", "Canina", "Cana", "Capito", "Carbo", "Catilina",
                           "Catula", "Celeris", "Celsa", "Cethega", "Cicurina", "Cilo", "Cincinnata", "Cinna",
                           "Corda", "Cornicen", "Cornuta", "Corvina", "Corva", "Cossa", "Costa", "Cotta",
                           "Crassipes", "Crispina", "Crispa", "Culleo", "Curio", "Cursor", "Curva", "Dentata",
                           "Dentra", "Dento", "Dives", "Dolabella", "Dorsuo", "Drusa", "Figula", "Fimbria",
                           "Flacca", "Flava", "Flora", "Fronto", "Fullo", "Fusa", "Galeo", "Gemella",
                           "Glabrio", "Graccha", "Gurges", "Habita", "Helva", "Iullus", "Labeo", "Lactuca",
                           "Laenas", "Lanata", "Laevina", "Laterensis", "Lentula", "Lepida", "Libo", "Licina",
                           "Longa", "Luculla", "Lurco", "Macra", "Macula", "Malleola", "Mamerca", "Marcella",
                           "Maro", "Merenda", "Merga", "Merula", "Messalla", "Metella", "Murena", "Mus",
                           "Musca", "Nasica", "Naso", "Natta", "Nepos", "Nerva", "Nigra", "Novella",
                           "Ocella", "Pacila", "Paeta", "Pansa", "Papa", "Patercula", "Paulla", "Pavo",
                           "Pera", "Pictrix", "Piso", "Planca", "Plauta", "Poplicola", "Postuma", "Potita",
                           "Praeconina", "Praetextata", "Prisca", "Procula", "Publicola", "Pulchra", "Pulla", "Pulvilla",
                           "Purpureo", "Quadrata", "Ralla", "Regilla", "Regula", "Rufa", "Ruga", "Rulla",
                           "Rutila", "Salinatrix", "Saturnina", "Scaeva", "Scaevola", "Scapula", "Scaura", "Scrofa",
                           "Severa", "Silana", "Silo", "Sila", "Stolo", "Strabo", "Structa", "Sura",
                           "Taura", "Triaria", "Trigemina", "Trio", "Tubero", "Tuberta", "Tubula", "Tuditana",
                           "Tulla", "Turda", "Varro", "Vara", "Vatia", "Verres", "Vespillo", "Vetus",
                           "Vitula", "Volusa"]

    praenomen = random.choice(praenomenlist_female) 
    nomen = random.choice(nomenlist)
    cognomen = random.choice(cognomenlist_female)

    return("%s %s %s" % (praenomen, nomen, cognomen))
