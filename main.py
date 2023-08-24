import support as sup




def main():
    # Verifica se o jogo está aberto, caso não esteja, ele abre.
    if sup.game_coords() != None:
        gsLeft, gsTop, gsRight, gsBottom = sup.game_coords()
        print("Pokemon está rodando nas coordenadas: L, T, R, B", gsLeft, gsTop, gsRight, gsBottom)
    else:
        print("Abrindo Pokemon...")
        sup.open_game()
        gsLeft, gsTop, gsRight, gsBottom = sup.game_coords()
        print("Pokemon está rodando nas coordenadas: L, T, R, B", gsLeft, gsTop, gsRight, gsBottom)

    
    sup.captureGameScreen(gsLeft, gsTop, gsRight, gsBottom)

    


if __name__ == "__main__":
    main()