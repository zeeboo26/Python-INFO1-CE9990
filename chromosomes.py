"""
dictionnary2.py

This program gives information on the different chromosomes of the human body.
"""
import sys

chromosomes = {
    "1": (3000, 240, 90, "Gauche disease, prostate cancer and glaucoma"),
    "2": (2500, 240, 95, "Colon cancer, essential tremor"),
    "3": (1900, 200, 95, "Lung cancer, VHL, MLH1"),
    "4": (1600, 190, 95, "Huntington and Parkinson, Narcolepsy"),
    "5":(1700, 180, 95, "Spinal muscular atrophy"),
    "6":(1900, 170, 95, "Spinocerebellar ataxia, diabetes, epilepsy"),
    "7":(1800, 150, 95, "Williams syndrome, cystic fibrosis, obesity"),
    "8":(1400, 140, 95, "Werner syndrome, burkitt lymphoma"),
    "9": (1400, 140, 85, "Malignant melanoma, tuberous sclerosis, FRDA"),
    "10":(1400, 130, 95, "Gyrate atrophy, refsum disease"),
    "11":(2000, 130, 95, "Best disease, MEN1, ATM, LQT"),
    "12":(1600, 130, 95, "Zellweger syndrome"),
    "13":(800, 110, 80, "Retinoblastoma, breast cancer, Wilson disease"),
    "14":(1200, 100, 80, "Alzheimer diease"),
    "15":(1200, 100, 80, "Tay-Sachs disease, Marfan syndrome"),
    "16":(1300, 90, 85, "Crohn's disease. PKD1"),
    "17":(1600, 80, 95, "Charcot-Marie-Tooth syndrome, breast cancer"),
    "18":(600, 70, 95, "Niemann-Pick disease, pancreatic cancer"),
    "19":(1700, 60, 85, "Severe combied immunodeficiency, atherosclerosis"),
    "20":(900, 60, 90, "ADA"),
    "21":(400, 40, 70, "Autoimmune polyglandular syndrome"),
    "22":(800, 40, 70, "Neurofibromatosis, chronic myeloid leukemia"),
    "X":(1400, 150, 95, "Menkes syndrome, fragile X syndrome, hemophilia"),
    "Y":(200, 50, 50, "Testes determining factor")
  
}

while True:
    try:
        chromosome = input("Please enter a chromosome: ")
        print()
    except EOFError:
        sys.exit(0)

    try:
        definition = chromosomes[chromosome]
    except KeyError:
        print("Sorry, \"", chromosome, "\" is not a known chromosome.", sep = "")
        print()
        continue   #Go back up to the word "while".
 
        
    
    print("Chromosome ", chromosome," contains ", definition[0], " genes, and has around ", definition[1], 
    " million base pairs of which ", definition [2], "% have been determined.", sep = "")
    print()
    print("Chromosome ", chromosome, " is associated with: ",definition[3],".", sep = "")
    print()
    if definition[2] < 95:
        print("Scientists need to do better research on chromosome ",chromosome,".", sep = "")
    if definition[2] <= 70:
        print("This is one of the chromosomes we know the less about.")
        print()
sys.exit(0)
