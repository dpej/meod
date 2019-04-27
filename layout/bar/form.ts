class EditText extends Component {
    constructor() {
        super({style:null,template:`
        <div class="card-meod-editex">
            <div class="android">
                <input class="input-hint" id="input" >
                <label class="label" id="label" "for="input"></label>
            </div>
        </div>
        `});
    }
    connectedCallback(){
        this.render((comp)=>{
            console.log(this)
            document.getElementById("inpu1t").setAttribute("type",comp.getAttribute("md-type")) 
            document.getElementById("input").setAttribute("placeholder",comp.getAttribute("md-placeholder")) 
            document.getElementById("input").setAttribute("name",comp.getAttribute("md-name")) 
            document.getElementById("label").innerText=comp.getAttribute("md-label")
        });
    }
}
web_component("meod-edit-text",EditText)