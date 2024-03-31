import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet, Alert, SafeAreaView, Image, TouchableOpacity } from 'react-native';
import utils from '../api/utils';
import { PrimaryButton, SecondButton } from '../components/Button';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import FormInput from '../components/FormInput';


const SignUpScreen = ({ navigation }) => {
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const [showPass, setShowPass]= React.useState('') 
  const [emailError, setEmailError]= React.useState('')
    const [usernameError, setusernameError]= React.useState('')
    const [passwordError, setPasswordError]= React.useState('')

  const handleSignUp = () => {
    // Simple validation
    if (!email || !name || !password) {
      Alert.alert('Error', 'Please fill in all fields');
      return;
    }

    console.log('Sign Up logic goes here');
    // Here you would typically handle the user registration logic,
    // such as sending the user details to your backend server

    // After successful signup, you can navigate to the login screen or directly into the app:
    // navigation.navigate('Login');
  };
  function isEnableSignUp(){
    return email != '' && name != '' && password != '' && emailError == '' &&
    passwordError == '' && usernameError == ''
}
  return (
    <SafeAreaView
    style={{
        flex:1,
        paddingVertical: 12,
        backgroundColor: 'white'
    }} 
    >
        <KeyboardAwareScrollView
        keyboardDismissMode='on-drag'
        contentContainerStyle={{
            flex:1,
            paddingHorizontal: 24
        }}>

            {/* App Icon */}

            <View 
            style={{
                alignItems:'center',
                marginTop:40
            }}>

                <Image 
                source={require('../assets/logo.webp')}
                resizeMode='contain'
                style={{
                    height: 200,
                    width:300
                }}/>

            </View>

            {/* Title */}

            <View
            style={{
                marginTop: 20,
                
            }} >

                <Text style={{
                    textAlign: 'center',
                     fontSize: 22, lineHeight: 30
                }}>
                    Getting Started
                </Text>

                <Text style={{
                    textAlign:'center',
                    color: 'gray',
                    marginTop:12,
                     fontSize: 16, lineHeight: 22
                }} >
                    Create an account to continue!
                </Text>

            </View>

            {/* Form Input and Signup*/}

            <View
            style={{
                flex:1,
                marginTop:10
            }} >
           <FormInput
           lable='Name'
           containerStyle={{
            marginTop: 10,
            marginBottom:8
           }}
           onChange={(value)=> {
                setName(value)
           }}
           errormsg={usernameError}
           appendComponent={
            <View
            style={{
                justifyContent:'center'
            }} 
            > 
                <Image 
                source={name == '' || 
                (name != '' && usernameError == '') ? 
                require('../assets/correct.png') : require('../assets/cancle.png')
                } style={{
                    height:20,
                    width:20,
                    tintColor: name=='' ? 'gray' : (name !='' && usernameError =='')? 'green': 'red',
                    }}
                />
            </View>
           } 
           />

        <FormInput 
          lable="Email" KeyboardType='email-address'
          autoCompleteType='email'
          onChange={(value) => {

            //validate email
            utils.validateEmail(value, setEmailError)

            setEmail(value)
          }}
          errormsg={emailError}
          appendComponent={
            <View 
            style={{
              justifyContent: 'center'
            }}>

              <Image 
              source={email == '' || (email != '' && emailError =='') ? require('../assets/correct.png') : require('../assets/cancle.png') }
              style={{
                width:20,
                height: 20,
                tintColor: email=='' ? 'gray' : (email !='' && emailError =='')? 'green': 'red',
              }}

              />

              </View>

          }
           />




            <FormInput 
           lable='Password'
           securetextEntry={!showPass}
           autoCompleteType='password'
           containerStyle={{
            marginTop: 10,
           }}
           onChange={(value) => {
                utils.validatePassword(value, setPasswordError)
                setPassword(value)
            }}
            errormsg={passwordError}
           appendComponent={
            <TouchableOpacity 
            style={{
              width:40,
              alignItems:'flex-end',
              justifyContent: 'center'
            }}
            onPress={()=> setShowPass(!showPass)}    >

            <Image 
              source={showPass ? require('../assets/eye_close.png'): require('../assets/eye.png')}
              style={{
                height: 20,
                width: 20,
                tintColor: 'gray'
              }}/>

            </TouchableOpacity>
           }
           />
            {/*Sign up & Sign In*/}

            <PrimaryButton
                title='Create account'
                disabled={isEnableSignUp() ? false : true}
                btnContainer={{
                    height: 55,
                    alignItems: 'center',
                    marginTop: 24,
                    borderRadius: 12,
                    backgroundColor: isEnableSignUp() ? 'orange' : 'rgba(227, 120, 75, 0.4)'
                }}
                onPress={handleSignUp} />

                <View
                style ={{
                    flexDirection: 'row',
                    marginTop: 12,
                    justifyContent: 'center'
                }} >

                    <Text style={{
                        color: 'gray',
                        fontSize: 16, lineHeight: 22
                    }} >
                        Already have an account?
                    </Text>
                    <SecondButton 
                    title='Login'
                    titlestyle={{
                        color: 'orange',
                        fontSize: 16, lineHeight: 22
                    }}
                    onPress={()=> navigation.goBack()}/>

                </View>
            </View>


            {/* Footer */}

            



        </KeyboardAwareScrollView>


    </SafeAreaView>
)


}

export default SignUpScreen;
