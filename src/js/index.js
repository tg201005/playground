
import MenuAPI from "./api.js";

const $ = (selector) => document.querySelector(selector);


function CaffeApp() {

    //execute
    this.menuAPI = new MenuAPI();
    this.menu = {
        espresso: [],
        frappuccino: [],
        blended: [],
        teavana: [],
        desert: [],
    };

    this.currentCategory = "espresso";



   //menu method

    const addMenu = async () => {
        await this.menuAPI.createMenu(this.currentCategory, $("#espresso-menu-name").value);
        const changedData = await this.menuAPI.getMenuData(this.currentCategory);
        this.menu[this.currentCategory] = changedData;
        render();
    };

    const updateMenu = async (e) => {
        //api -> js -> html
        const menuId = e.target.closest("li").dataset.menuId;
        let updatedMenuName = prompt("메뉴명을 수정하세요");
        await this.menuAPI.updateMenu(this.currentCategory, menuId, updatedMenuName);
        const changedData = await this.menuAPI.getMenuData(this.currentCategory);
        console.log(changedData);
        this.menu[this.currentCategory] = changedData;
        render();   
    };

    const removeMenu = async (e) => {
        //api -> js -> html
        //menu index
        const menuId = e.target.closest("li").dataset.menuId;
        await this.menuAPI.deleteMenu(this.currentCategory, menuId);
        const changedData = await this.menuAPI.getMenuData(this.currentCategory);
        this.menu[this.currentCategory] = changedData;
        render();
    };

    const soldOut = async (e) => {
      //api -> js -> html
      //menu index
    
        const menuId = e.target.closest("li").dataset.menuId;
        await this.menuAPI.soldOutMenu(this.currentCategory, menuId);
        const changedData = await this.menuAPI.getMenuData(this.currentCategory);
        this.menu[this.currentCategory] = changedData;
        render();      
    };


    const eventListener = () =>{

        $("#espresso-menu-form").addEventListener("submit", (e) => { e.preventDefault();});
        $("#espresso-menu-submit-button").addEventListener("click", addMenu());
        $("#nav").addEventListener("click", (e) => {switchCategory(e);});
        $("#espresso-menu-list").addEventListener("click", (e) => {
            switch (true) {
                case e.target.classList.contains("menu-edit-button"):
                    updateMenu(e);
                    break;
                case e.target.classList.contains("menu-remove-button"):
                    removeMenu(e);
                    break;
                case e.target.classList.contains("menu-soldout-button"):
                    soldOut(e);
                    break;
                default:
                    break;
            }
        });
    };
    $("#espresso-menu-name").addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            e.preventDefault();
            addMenu();
        }
    });



        //menu

        //add, delete, update Menu


    const render = () =>{
        //make menu html
        const menuList = this.menu[this.currentCategory].map((menu, index) => {
            return `
            <li data-menu-id="${menu.id}" class="menu-list-item d-flex items-center py-2 ${
                menu.isSoldOut ? "sold-out" : ""}" style="justify-content: flex-end;">
                <span class="w-100 pl-3 menu-name">${menu.name}</span>
                <button type="button" class="bg-gray-50 text-gray-500 text-sm mr-1 menu-soldout-button">${menu.isSoldOut ? "판매중" : "품절"}</button>
                <button type="button" class="bg-gray-50 text-gray-500 text-sm mr-1 menu-edit-button"> 수정 </button>
                <button type="button" class="bg-gray-50 text-gray-500 text-sm menu-remove-button"> 삭제 </button>
            </li>`;
        }).join("");
        $("#espresso-menu-list").innerHTML = menuList;
        $("#espresso-menu-name").value = "";       
    };

        //method for switching category
    const switchCategory = async (e) => {
        //api -> js -> html
        this.currentCategory = e.target.dataset.categoryName;
        this.menu[this.currentCategory] = await this.menuAPI.getMenuData(this.currentCategory);
        $("#menu-manager").innerText = `${e.target.innerText} 메뉴 관리`;
        render();
    };
    
    // execute
    render();
    eventListener();
};

const app = new CaffeApp();