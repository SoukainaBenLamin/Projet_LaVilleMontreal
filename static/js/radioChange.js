function onGlissadeRadioSelect() {
    var glissades_radio = document.getElementById("radio_glis");
    var select = document.getElementById("champ-installation");
        if (glissades_radio.checked) {
            select = clearSelect(select);
            select.value = "";
            select.disabled = false;
            option = document.createElement("option");
            option.text = "selectionner un glissade";
            select.appendChild(option);
            fetch("/api/installations/glissades")
                .then(response => response.json())
                .then(response => {
                    for(let i = 0; i < response.glissades.length; i++) {
                        option = document.createElement("option");
                        option.text = response.glissades[i].nom;
                        option.value = i
                        select.appendChild(option);
                    }

                })

        }
 }
 function onPiscineRadioSelect() {
    var piscines_radio = document.getElementById("radio_pis");
    var select = document.getElementById("champ-installation");
        if (piscines_radio.checked) {
            select = clearSelect(select);
            select.value = "";
            select.disabled = false;
            option = document.createElement("option");
            option.text = "selectionner une piscine";
            select.appendChild(option);
            fetch("/api/installations/piscines")
                .then(response => response.json())
                .then(response => {
                    for(let i = 0; i < response.piscines.length; i++) {
                        option = document.createElement("option");
                        option.text = response.piscines[i].nom;
                        option.value = i
                        select.appendChild(option);
                    }
                })
 }
 }

 function onPatinoireRadioSelect() {
    var patinoires_radio = document.getElementById("radio_pat");
    var select = document.getElementById("champ-installation");
        if (patinoires_radio.checked) {
            select = clearSelect(select);
            select.value = "";
            select.disabled = false;
            option = document.createElement("option");
            option.text = "selectionner un patinoire";
            select.appendChild(option);
            fetch("/api/installations/patinoires")
                .then(response => response.json())
                .then(response => {
                    for(let i = 0; i < response.patinoires.length; i++) {
                        option = document.createElement("option");
                        option.text = response.patinoires[i].nom;
                        option.value = i
                        select.appendChild(option);
                    }
                })
 }
 }

function clearSelect(selectElem) {
    if (selectElem.hasChildNodes() ) {
        selectElem.innerHTML = "";
    }
    return selectElem;
}

function onChangeSelect() {
    document.getElementById("dvGlis").style.display = "none";
    document.getElementById("dvPis").style.display = "none";
    document.getElementById("dvPat").style.display = "none";
    var select = document.getElementById("champ-installation");
    var name = select.options[select.selectedIndex].text;
    if (document.getElementById("radio_glis").checked) {
        document.getElementById("dvGlis").style.display = "block";
         fetch("/api/glissade/"+name)
                .then(response => response.json())
                .then(response => {
                    document.getElementById("name_g").innerHTML = response.infos[0].Nom;
                    document.getElementById("arrond_g").innerHTML  = response.infos[0].Arrondissement;
                    document.getElementById("cle").innerHTML = response.infos[0].Cle;
                    document.getElementById("condition").innerHTML = response.infos[0].Condition;
                    document.getElementById("date").innerHTML = response.infos[0].Date;
                    document.getElementById("deblaye").innerHTML = response.infos[0].Deblaye;
                    document.getElementById("ouvert").innerHTML = response.infos[0].Ouvert;

                })
    }
    else if (document.getElementById("radio_pis").checked) {
        document.getElementById("dvPis").style.display = "block";
        fetch("/api/piscine/"+name)
                .then(response => response.json())
                .then(response => {
                    document.getElementById("name_pis").innerHTML = response.infos[0].Nom;
                    document.getElementById("arrond_pis").innerHTML  = response.infos[0].Arrondissement;
                    document.getElementById("id").innerHTML = response.infos[0].Id;
                    document.getElementById("adresse").innerHTML = response.infos[0].Adresse;
                    document.getElementById("prop").innerHTML = response.infos[0].Propriété;
                    document.getElementById("type").innerHTML = response.infos[0].Type;
                })
    }
    else if (document.getElementById("radio_pat").checked) {
        document.getElementById("dvPat").style.display = "block";
        fetch("/api/patinoire/"+name)
                .then(response => response.json())
                .then(response => {
                    document.getElementById("name_pat").innerHTML = response.infos[0].Nom;
                    document.getElementById("arrond_pat").innerHTML  = response.infos[0].Arrondissement;
                    document.getElementById("date_p").innerHTML = response.infos[0].Date;
                    document.getElementById("deblaye_p").innerHTML = response.infos[0].Deblaye;
                    document.getElementById("ouvert_p").innerHTML = response.infos[0].Ouvert;
                    document.getElementById("arrose").innerHTML = response.infos[0].Arrose;
                    document.getElementById("resurface").innerHTML = response.infos[0].resurface;
                })
    }

}

document.getElementById("radio_glis").addEventListener("click", onGlissadeRadioSelect);
document.getElementById("radio_pis").addEventListener("click", onPiscineRadioSelect);
document.getElementById("radio_pat").addEventListener("click", onPatinoireRadioSelect);
document.getElementById("champ-installation").addEventListener('change', onChangeSelect);