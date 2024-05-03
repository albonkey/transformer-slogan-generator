import { Text, View, TextInput } from 'react-native'
import React, { Component } from 'react'






const FormInput=( {

    containerStyle,
    lable,
    placeholder,
    inputStyle,
    prependComponent,
    appendComponent,
    onChange,
    securetextEntry,
    KeyboardType = 'default',
    autoCompleteType = 'off',
    autoCapitalize= 'none',
    errormsg= ''

}) => {
    return (
        <View style={{...containerStyle}}>

            {/* lable and error msg */}
            <View 
            style={{
                flexDirection: 'row',
                justifyContent: 'space-between'
            }}>

                <Text style={{color: 'gray',  fontSize:14, lineHeight: 22 }} >
                    {lable}
                </Text>
                <Text style={{color: 'red',  fontSize:14, lineHeight: 22 }} >
                    {errormsg}
                </Text>

            </View>

            {/* Text Input */}

            <View 
            style={{
                flexDirection:'row',
                height: 55,
                paddingHorizontal: 24,
                marginTop: 8,
                borderRadius: 24,
                backgroundColor: 'lightgray',
                
            }}>

                {prependComponent}

                <TextInput 
                style={{
                    flex: 1,
                    ...inputStyle
                }}
                placeholder={placeholder}
                placeholderTextColor={'white'}
                secureTextEntry={securetextEntry}
                KeyboardType={KeyboardType}
                autoCompleteType={autoCompleteType}
                autoCapitalize={autoCapitalize}
                onChangeText={(text) => onChange(text)}
                />

                {appendComponent}

            </View>
          
        </View>
      )
    
}


export default FormInput;