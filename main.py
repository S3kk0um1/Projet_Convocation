import pandas as pd
import words_manip
def pdfscrape(pdf):
    # Extract each relevant information individually
    nom= pdf.pq('LTTextLineHorizontal:overlaps_bbox("288.96, 618.603, 492.975, 631.273")').text()#[288.96, 618.603, 492.975, 631.273]313.2, 644.452, 462.709, 656.952
    CIN= pdf.pq('LTTextLineHorizontal:overlaps_bbox("343.92, 629.163, 426.524, 640.163")').text()
    ecole = pdf.pq('LTTextLineHorizontal:overlaps_bbox("309.12, 612.019, 463.592, 623.76")').text()
    spe= pdf.pq('LTTextLineHorizontal:overlaps_bbox("222.0, 472.443, 282.522, 483.443")').text()
    niveau= pdf.pq('LTTextLineHorizontal:overlaps_bbox("221.76, 446.556, 369.003, 458.556")').text()
    periode = pdf.pq('LTTextLineHorizontal:overlaps_bbox("223.92, 425.333, 371.68, 437.833")').text()
    direc= pdf.pq('LTTextLineHorizontal:overlaps_bbox("223.68, 403.563, 416.489, 415.523")').text()
    serv= pdf.pq('LTTextLineHorizontal:overlaps_bbox("223.68, 382.307, 243.515, 392.807")').text()
    parrain= pdf.pq('LTTextLineHorizontal:overlaps_bbox("223.92, 360.707, 324.404, 372.083")').text()

    ecole=words_manip.delete_before_character(ecole,'e')
    periode=words_manip.delete_words_regex(periode,["du","au"])
    periode=words_manip.delete_spaces(periode)
    periode=words_manip.modify_letter(periode,2,"-")
    periode = words_manip.modify_letter(periode,5,"-")
    periode= words_manip.modify_letter(periode, 12, "-")
    periode= words_manip.modify_letter(periode,15,"-")
    periode = words_manip.add_space_at_index(periode, 10)
    periode=periode.split()
# Combined all relevant information into single observation
    page = pd.DataFrame({
                         'Nom': words_manip.delete_before_character(nom," ").split()[1],
                         'Prenom': words_manip.delete_before_character(nom, " ").split()[0],
                         'CIN': words_manip.delete_before_character(CIN,":"),
                         'Ecole': ecole,
                         'Specialité': spe,
                         'Niveau d\'etude': niveau,
                         'Periode de stage du': periode[0],
                         'Au': periode[1],
                         'Direction d\'accueil':direc,
                         'Service d\'accueil': serv,
                         'Parrain': parrain

                       }, index=[0])
    return(page)