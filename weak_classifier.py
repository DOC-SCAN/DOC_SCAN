import pytesseract
import glob
from PIL import Image

a = "HISTORY &"
aa = "PHYSICAL EXAMINATION"
b = "SAFE PROCEDURE CHECKLIST"
c = "Mandibular"
d = "Maxillary"
e = "REFUSES to be marked"
f = "CHECK-IN"
g = "SIGN OUT"
h = "Any equipment problems to be"
i = "GRAPHICAL ASSESSMENT"
j = "BSR"
k = "Pain Score"
l = "PEWS"
m = "INITIAL NURSING ASSESSMENT"
n = "Adult Early Warning Scores"
o = "SPO2 Oxygen Saturation"
p = "History of Present Illness :"
q = "Patient Medical Record"
r = "Personal Information Chart"
s = "Extremities & Blood Vessels"
t = "Signature of Medical Officer :"
u = "Signature of Attending Physician :"
v = "PHYSICIAN'S PROGRESS RECORD"
w = "Physician's Progress Record"
x = "PATIENT REGISTRATION FORM"
y = "The patient(has) read this authorization"
z = "Name of Person/ Organization?"
a1 = "Modified Glasgow Coma Scale"
a2 = "CRY"
a3 = "ARS"
a4 = "LEGS"
a5 = "ALERTNESS"
a6 = "Best verbal response"
a7 = "Best motor response"
a8 = "NEUROLOGICAL ASSESSMENT"
a9 = "CRV"
a10 = "Head Injury"
a11 = "Seizures"


def classify(imgpath):
    for filename in glob.glob(imgpath):
        check = pytesseract.image_to_string(Image.open(filename), lang='eng')
        print("Checking " + filename)
        if (b or c or d or e or f or g) in check:
            return 'BED SIDE PROCEDURE'
        elif (aa or a or p or s or t or u) in check:
            return 'HISTORY AND PHYSICAL'
        elif (q or r) in check:
            return 'OLD FACE SHEET'
        elif (v or w) in check:
            return 'PHYSICIAN PROGRESS RECORD'
        elif (x or y or z) in check:
            return 'PATIENT REGISTRATION FORM'
        elif (a1 or (a2 and a3 and a4 and a5) or (a6 and a7)) in check:
            return 'MODIFIED GLASGOW COMA SCALE'
        elif (a8 or a9 or (a10 and a11)) in check:
            return 'HISTORY AND PHYSICAL'
        else:
            return ''
