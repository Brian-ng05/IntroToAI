class Get_outfit:
    outfit_suggestions = {
     "Male": {
            "School": {
                "SmartCasual":     "T-shirt or basic blouse "
                                    "\nStraight jeans "
                                    "\nSneakers or casual slip-on shoes "
                                    "\nBackpack "
                                    "\nMinimal accessories: digital watch",
                "Elegant":          "Shirt with soft collar "
                                    "\nCulottes or tailored shorts "
                                    "\nLoafers "
                                    "\nAccessories: slim watch"
            },
            "Work": {
                "SmartCasual":     "Long sleeve shirt "
                                    "\nOxford shoes "
                                    "\nWatch, narrow beltfaced watch "
                                    "\nsmall leather belt",
                "Elegant":          "Polo shirt / relaxed shirt "
                                    "\nKhaki pants, straight-leg pants "
                                    "\nSneakers / Loafers "
                                    "\nSimple accessories: minimalist watch"
            },
            "Party": {
                "SmartCasual":     "Casual shirt"
                                    "\nSlim-fit jeans"
                                    "\nSneakers / loafers"
                                    "\nAccessories: watch, simple",
                "Elegant":          "Dress shirt"
                                    "\nDress pants, Oxford shoes or leather loafers"
                                    "\nAccessories: watch, subtle perfume"
            }
        },
        "Female": {
            "School": {
                "SmartCasual":     "T-shirt or basic blouse "
                                    "\nStraight jeans or pleated skirt "
                                    "\nSneakers or casual slip-on shoes "
                                    "\nTote bag "
                                    "\nMinimal accessories: scrunchie, digital watch",
                "Elegant":          "Light knit top "
                                    "\nMidi skirt, culottes "
                                    "\nDoll shoes or loafers "
                                    "\nCrossbody bag or mini handbag "
                                    "\nAccessories: ribbon tie, minimalist necklace, slim watch"
            },
            "Work": {
                "SmartCasual":     "Long sleeve shirt/blouse "
                                    "\nTrousers or midi skirt "
                                    "\nHigh heels"
                                    "\nWatch, handbag or narrow beltfaced watch, small leather belt",
                "Elegant":          "Polo shirt / relaxed shirt or light blouse "
                                    "\nStraight-leg pants, A-line skirt "
                                    "\nSneakers / Loafers / Doll shoes "
                                    "\nSimple accessories: tote bag, minimalist watch"
            },
            "Party": {
                "SmartCasual":     "Casual shirt / printed blouse / knit top"
                                    "\nSlim-fit jeans or midi skirt"
                                    "\nSneakers / ankle boots / loafers"
                                    "\nCrossbody or shoulder bag"
                                    "\nAccessories: watch, simple earrings or rings",
                "Elegant":          "Dress shirt or fitted top / satin blouse"
                                    "\nDress pants, pencil skirt, or cocktail dress Heels"
                                    "\nClutch bag or sleek handbag"
                                    "\nAccessories: statement necklace, watch, subtle perfume"
            }
        }
    }

    @staticmethod
    def Get_outfit(input: list[str]) -> str:
        GENDER_INPUT = input[0]
        OCCASION_INPUT = input[1]
        STYLE_INPUT = input[2]

        return Get_outfit.outfit_suggestions[GENDER_INPUT][OCCASION_INPUT][STYLE_INPUT]