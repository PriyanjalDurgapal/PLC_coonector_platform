import { defineStore } from "pinia"


export const useThemeStore = defineStore(
"theme",
{

state:()=>({

    mode:
    localStorage.getItem("theme")
    || "light"

}),



actions:{


    init(){


        document.documentElement.classList.toggle(
            "dark",
            this.mode==="dark"
        )


    },


    toggle(){


        this.mode =
        this.mode==="light"
        ? "dark"
        : "light"


        localStorage.setItem(
            "theme",
            this.mode
        )


        document.documentElement.classList.toggle(
            "dark",
            this.mode==="dark"
        )


    }


}


})