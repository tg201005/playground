const BASE_URL = "http://localhost:8000/api";

class MenuAPI {

    getMenuData = async (categoryName) => {
        const response = await fetch(`${BASE_URL}/category/${categoryName}/menu`);
        return await response.json();
    };

    createMenu = async (categoryName, menuName) => {
        const response = await fetch(`${BASE_URL}/category/${categoryName}/menu`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ name: menuName }),
        });
        if (!response.ok) {
            console.error("메뉴 생성 실패");
            console.log(response);
        }
    };

    deleteMenu = async (categoryName, menuId) => {
        const response = await fetch(`${BASE_URL}/category/${categoryName}/menu/${menuId}`, {
            method: "DELETE",
        });
        return (await this.getMenuData(categoryName));
    };

    updateMenu = async (categoryName, menuId, menuName) => {
        const response = await fetch(`${BASE_URL}/category/${categoryName}/menu/${menuId}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ name: menuName }),
        });
    };

    soldOutMenu = async (categoryName, menuId) => {
        const response = await fetch(`${BASE_URL}/category/${categoryName}/menu/${menuId}/soldout`, {
            method: "PUT",
        });
    };
}

export default MenuAPI;