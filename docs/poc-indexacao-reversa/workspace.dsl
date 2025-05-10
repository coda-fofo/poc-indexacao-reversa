workspace {
    model {
        !include ./properties.dsl

        group "PoC Indexação Reversa" {
            !include "containers.dsl"
            !include "relationships.dsl"
        }
    }

    views {
        !include "views.dsl"

        systemLandscape "PoCLandscape" {
            include "element.tag==motor_busca"
            autoLayout
        }

        styles {
            !include ./styles.dsl
        }
    }
}