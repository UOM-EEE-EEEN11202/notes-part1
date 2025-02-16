window.onload = function() {
    if (localStorage.getItem("alt-font-store") === "True") {
        document.body.classList.toggle("alt-font");
        document.getElementById("uom_header_title").classList.toggle("alt-font");
        document.getElementById("uom_header_buttons").classList.toggle("alt-font");
        document.getElementById("uom_footer_info").classList.toggle("alt-font");
        document.getElementById("default-font").classList.add("alt-font-display");
        document.getElementById("alt-font").classList.add("alt-font-nodisplay");
    }
    else {
        document.getElementById("default-font").classList.add("alt-font-nodisplay");
        document.getElementById("alt-font").classList.add("alt-font-display");
    }
};

document.getElementById("uom_alt_font_button").addEventListener("click",
function(){
    document.body.classList.toggle("alt-font");
    document.getElementById("uom_header_title").classList.toggle("alt-font");
    document.getElementById("uom_header_buttons").classList.toggle("alt-font");
    document.getElementById("uom_footer_info").classList.toggle("alt-font");
    
    if (document.body.classList.contains("alt-font")) {
        document.getElementById("default-font").classList.remove("alt-font-nodisplay");
        document.getElementById("default-font").classList.add("alt-font-display");
        document.getElementById("alt-font").classList.remove("alt-font-display");
        document.getElementById("alt-font").classList.add("alt-font-nodisplay");
        localStorage.setItem("alt-font-store", "True");
    }
    else{
        document.getElementById("default-font").classList.remove("alt-font-display");
        document.getElementById("default-font").classList.add("alt-font-nodisplay");
        document.getElementById("alt-font").classList.remove("alt-font-nodisplay");
        document.getElementById("alt-font").classList.add("alt-font-display");
        localStorage.setItem("alt-font-store", "False");
    }
});