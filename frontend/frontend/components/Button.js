import React from "react";
import { View, StyleSheet, Text, TouchableOpacity} from "react-native";




const PrimaryButton = ({title,disabled,btnContainer, onPress = () => {}}) =>{

    return <TouchableOpacity style={{
        backgroundColor: 'orange',
        justifyContent: 'center',                
         alignItems: 'center', 
         ...btnContainer
         }}
          activeOpacity={0.8}  onPress={onPress} disabled={disabled}>
        <View >
            <Text style={styles.title}>{title} </Text>
        </View>
    </TouchableOpacity>


}
const SecondButton = ({title,disabled, btnContainer,titlestyle, onPress = () => {}}) =>{

    return <TouchableOpacity style={{ 
        backgroundColor: 'orange',
        borderRadius: 30,
        justifyContent: 'center',
        alignItems: 'center',
         backgroundColor: 'white',
        ...btnContainer}}
         activeOpacity={0.8} onPress={onPress} disabled={disabled}> 
        <View >
            <Text style={{
                color:'white',
                fontWeight:'bold',
                fontSize:18,
                color: 'gray', 
                fontSize:15,
                ...titlestyle,
                 }}>{title} </Text>
        </View>
    </TouchableOpacity>


}

const styles = StyleSheet.create({
    
    
    title:{
        color:'white',
        fontWeight:'bold',
        fontSize:18,

    }
})

export  {PrimaryButton, SecondButton};