const lista= document.getElementById('program_content');
const lista2= document.getElementById('strategies');



new Sortable(lista, {
    group:'group1',
    multiDrag: true, // Enable multi-drag
	selectedClass: 'selected', // The class applied to the selected items
	fallbackTolerance: 3,
    animation: 150,
    ghostClass: 'blue-background-class',
    chosenClass:"select",
    onEnd: ()=> {
        console.log("se solto un elemento")
    },
    group:"lista-elemento",
    store: {
        //guarda orden de lista (de manera local, alfredo lo hara en la base de datos)
        set: (sortable)=>{
            const orden= sortable.toArray();
            localStorage.setItem(sortable.options.group.name,orden.join("/"));  //el orden se guarda en forma de array pero el metodo necesita un string, por eso el join
        },
        // retorna el orden 
        get: (sortable) => {
            const orden =localStorage.getItem(sortable.options.group.name);
            return orden ? orden.split("/") : []; //el orden  esta almacenado aqui com string pero el metodo necesita un array, por eso el jsplit
        }
    }
});

new Sortable(lista2, {
    group:'group2',
    multiDrag: true, // Enable multi-drag
	selectedClass: 'selected', // The class applied to the selected items
	fallbackTolerance: 3,
    animation: 150,
    ghostClass: 'blue-background-class',
    chosenClass:"select",
    onEnd: ()=> {
        console.log("se solto un elemento")
    },
    group:"lista-elemento2",
    store: {
        //guarda orden de lista (de manera local, alfredo lo hara en la base de datos)
        set: (sortable)=>{
            const orden= sortable.toArray();
            localStorage.setItem(sortable.options.group.name,orden.join("/"));  //el orden se guarda en forma de array pero el metodo necesita un string, por eso el join
        },
        // retorna el orden 
        get: (sortable) => {
            const orden =localStorage.getItem(sortable.options.group.name);
            return orden ? orden.split("/") : []; //el orden  esta almacenado aqui com string pero el metodo necesita un array, por eso el jsplit
        }
    }
});