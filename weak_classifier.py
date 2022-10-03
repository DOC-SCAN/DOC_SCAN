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
xx = "PHYSICIANS PROGRESS RECORD"
xx1 = "Progress Record"
xxx = "PROGRESS RECORD"
y = "The patient have(has) read this authorization"
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
a12 = "AUTHORIZATION AND CONSENT FOR"
a13 = "Treatment may include physical examination, diagnostic"
a14 = "I agree that if I (Patient) do not visit the hospital for treatment"


def classify(image_path):
    for filename in glob.glob(image_path):
        check = pytesseract.image_to_string(Image.open(filename), lang='eng')
        print("Checking " + filename)
        if b in check:
            return 'BED SIDE PROCEDURE'
        elif c in check:
            return 'BED SIDE PROCEDURE'
        elif d in check:
            return 'BED SIDE PROCEDURE'
        elif e in check:
            return 'BED SIDE PROCEDURE'
        elif f in check:
            return 'BED SIDE PROCEDURE'
        elif g in check:
            return 'BED SIDE PROCEDURE'
        elif aa in check:
            return 'HISTORY AND PHYSICAL'
        elif a in check:
            return 'HISTORY AND PHYSICAL'
        elif p in check:
            return 'HISTORY AND PHYSICAL'
        elif s in check:
            return 'HISTORY AND PHYSICAL'
        elif t in check:
            return 'HISTORY AND PHYSICAL'
        elif u in check:
            return 'HISTORY AND PHYSICAL'
        elif q  in check:
            return 'OLD FACE SHEET'
        elif r in check:
            return 'OLD FACE SHEET'
        elif xxx in check:
            return 'PHYSICIAN PROGRESS RECORD'
        elif xx1 in check:
            return 'PHYSICIAN PROGRESS RECORD'
        elif v in check:
            return 'PHYSICIAN PROGRESS RECORD'
        elif w in check:
            return 'PHYSICIAN PROGRESS RECORD'
        elif xx in check:
            return 'PHYSICIAN PROGRESS RECORD'
        elif x in check:
            return 'PATIENT REGISTRATION FORM'
        elif y in check:
            return 'PATIENT REGISTRATION FORM'
        elif z in check:
            return 'PATIENT REGISTRATION FORM'
        elif a1 in check:
            return 'MODIFIED GLASGOW COMA SCALE'
        elif (a2 and a3 and a4 and a5) in check:
            return 'MODIFIED GLASGOW COMA SCALE'
        elif (a6 and a7) in check:
            return 'MODIFIED GLASGOW COMA SCALE'
        elif (a8 or a9 or (a10 and a11)) in check:
            return 'HISTORY AND PHYSICAL'
        elif a9 in check:
            return 'HISTORY AND PHYSICAL'
        elif (a10 and a11) in check:
            return 'HISTORY AND PHYSICAL'
        elif (a12 or a13 or a14) in check:
            return 'CONSENT FORM'
        elif a12 in check:
            return 'CONSENT FORM'
        elif a13 in check:
            return 'CONSENT FORM'
        elif a14 in check:
            return 'CONSENT FORM'
        else:
            return None
