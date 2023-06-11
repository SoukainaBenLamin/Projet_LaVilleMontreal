function onSubmitForm() {
    event.preventDefault();
    var div = document.getElementById("DvError");
    var element = document.getElementById("table");
    tabBody1=document.getElementById("glissade_tab");
    tabBody2=document.getElementById("piscine_tab");
    tabBody3=document.getElementById("patinoire_tab");
    if (tabBody1.hasChildNodes()) {
        tabBody1.innerHTML = "";
    }
    if (tabBody2.hasChildNodes()) {
        tabBody2.innerHTML = "";
    }
     if (tabBody3.hasChildNodes()) {
        tabBody3.innerHTML = "";
    }
    var arron= document.getElementById("search").elements['champ-arrondis'].value;
    var str = "?arrondissement="+arron;
    fetch("/api/installations"+str)
        .then(response => response.json())
        .then(response => {
            if (response.hasOwnProperty('vide')){
                element.style.display = "none";
                div.style.display = "block";
            }
            else {
                div.style.display = "none";
                tabBody1=document.getElementsByTagName("tbody").item(1);
                for(let i = 0; i < response.glissades.length; i++){
                    row=document.createElement("tr");
                    cell1 = document.createElement("td");
                    textnode1=document.createTextNode(response.glissades[i].nom);
                    cell1.appendChild(textnode1);
                    row.appendChild(cell1);
                    tabBody1.appendChild(row);
                }
                tabBody2=document.getElementsByTagName("tbody").item(2);
                for(let i = 0; i < response.piscines.length; i++){
                    row=document.createElement("tr");
                    cell1 = document.createElement("td");
                    textnode1=document.createTextNode(response.piscines[i].nom);
                    cell1.appendChild(textnode1);
                    row.appendChild(cell1);
                    tabBody2.appendChild(row);
                }
                tabBody3=document.getElementsByTagName("tbody").item(3);
                for(let i = 0; i < response.patinoires.length; i++){
                    row=document.createElement("tr");
                    cell1 = document.createElement("td");
                    textnode1=document.createTextNode(response.patinoires[i].nom);
                    cell1.appendChild(textnode1);
                    row.appendChild(cell1);
                    tabBody3.appendChild(row);
                }
                element.style.display = "block";
            }
        })
        .catch(err => {
            console.log("Erreur avec le serveur :", err);
        });
        document.getElementById("search").reset();
    }
var element = document.getElementById("table");
element.style.display = "none";
document.getElementById("search").addEventListener("submit", onSubmitForm);
