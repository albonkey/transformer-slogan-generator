import { Text, View, TouchableWithoutFeedback, StyleSheet } from 'react-native'
import React from 'react'

 const Switch =({value, onChange}) => {
  
    return (
      <TouchableWithoutFeedback onPress={()=> onChange(!value)}>
        <View 
            style={{
                flexDirection: 'row'
            }}>

                {/*Switch*/}
                <View 
                style={value ? style.switchOnContainer : style.switchOffContainer} >

                    <View 
                        style={{
                            ...style.dot,
                            backgroundColor: value ? 'white' : 'gray'
                        }}>

                    </View>

                </View>
                {/*Text*/}

                <Text 
                    style={{
                        color: value ? 'orange' : 'gray',
                        marginLeft: 8, fontSize: 14, lineHeight: 22

                    }} >
                        Save Me

                </Text>

        </View>


      </TouchableWithoutFeedback>
    )
  
}

const style= StyleSheet.create({

    switchOnContainer:{
        width:40,
        height:20,
        paddingRight: 2,
        justifyContent: 'center',
        alignItems: 'flex-end',
        borderRadius: 10,
        backgroundColor: 'orange',
        
    },
    switchOffContainer:{
        width:40,
        height:20,
        paddingRight: 2,
        justifyContent: 'center',
        
        borderRadius: 10,
        borderColor: 'gray',
        borderWidth: 1,
        
        
    },

    dot:{
        width:12,
        height:12,
        borderRadius: 6,
        marginHorizontal:2
    }
})


export default Switch;