import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Stack(
            [
                ft.Image(
                    src="https://picsum.photos/800/400",
                    width=800,
                    height=400,
                ),
                ft.Text(
                    "Demo of Flet Splash!",
                    size=40,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE,
                    bgcolor=ft.Colors.WHITE,
                ),
            ],
            expand=True,
            alignment=ft.Alignment.CENTER,
        ),
    )


if __name__ == "__main__":
    ft.run(main)
