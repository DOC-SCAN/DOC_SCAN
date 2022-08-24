import cx_Oracle
import pandas as pd
import json


def ipd_patient_details():
    dsn_tns = cx_Oracle.connect('asad_25510/asad#123@developdb.shifa.com.pk:1521/devdata.shifa.com.pk')
    cursor = dsn_tns.cursor()
    lis = list()
    mr = "958005"
    mr = "'" + mr + "'"
    query = "SELECT cn.pc, cn.visit_id, a.fld_dat_adm_date, sp.speciality_name, d.doctor_id, d.consultant from " \
            "ADMISSION.TBL_ADMISSION A, emr.const_notes         CN, doctors                 d,  specialities            " \
            "sp  WHERE a.pk_str_admission_id = cn.id_ and a.fk_int_admitting_dr_id = d.doctor_id  and " \
            "d.primary_speciality_id = sp.speciality_id  and a.mr# = " + mr
    for row in cursor.execute(query):
        df = pd.DataFrame(row, index=['Patient_Complain', 'Admission_ID', 'Admission_Data', 'Admitted_In_Speciality',
                                      'Admitting_doctor_ID', 'Admitting_Doctor_Name'], )
        lis.append(((pd.DataFrame.to_json(df, orient='columns')).replace('"', "'"))[5:-1])
    return lis


if __name__ == '__main__':
    ipd_patient_details()
