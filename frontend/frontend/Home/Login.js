import React,{useState} from 'react';
import { View, Text, TextInput, Button, StyleSheet, SafeAreaView, Image, TouchableOpacity } from 'react-native';
import utils from '../api/utils';
import FormInput from '../components/FormInput'
import { PrimaryButton } from '../components/Button';

const LoginScreen = ({ navigation }) => {
    const [emailError, setEmailError] = React.useState('')
    const [email, setEmail] = React.useState('')
    const [password, setPassword] = React.useState('')
    const [showPass, setShowPass] = React.useState(false)

    function isEnableSignIn() { return email != '' && password != '' && emailError == '' }
  return (
    <SafeAreaView style={styles.container}>

      <Text style={styles.title}>Login</Text>
      <View
          style={{
            alignItems: 'center',
            margin:20
            
          }}>
        <Image
            source={require('../assets/logo.webp')}
            resizeMode='contain'
            style={{
              height: 200,
              width: 300
            }} />

        </View>
        <View
          style={{
            flex: 1,
            marginHorizontal:10
          }}>
        <FormInput
            lable="email" KeyboardType='email-address'
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
                  source={email == '' || (email != '' && emailError == '') ? require('../assets/correct.png') : require('../assets/cancle.png')}
                  style={{
                    width: 20,
                    height: 20,
                    tintColor: email == '' ? 'gray' : (email != '' && emailError == '') ? 'green' : 'red',
                  }}

                />

              </View>

            }
          />
        <FormInput
            lable='password'
            securetextEntry={!showPass}
            autoCompleteType='password'
            containerStyle={{
              marginTop: 24,
            }}
            onChange={(value) => setPassword(value)}
            appendComponent={
              <TouchableOpacity
                style={{
                  width: 40,
                  alignItems: 'flex-end',
                  justifyContent: 'center'
                }}
                onPress={() => setShowPass(!showPass)}    >

                <Image
                  source={showPass ? require('../assets/eye_close.png') : require('../assets/eye.png')}
                  style={{
                    height: 20,
                    width: 20,
                    tintColor: 'gray'
                  }} />

              </TouchableOpacity>
            }
          />
            </View>
        <View style={{ alignSelf: 'center',  }}>
            <PrimaryButton
              btnContainer={{

                backgroundColor: isEnableSignIn() ? 'orange' : 'rgba(227, 120, 75, 0.4)',
                height: 55, width: 200,
                borderRadius: 24,
                

              }}
              title='Login'

              disabled={isEnableSignIn() ? false : true}
              //check with firebase
              onPress={() => console.log('Login')} 
                
              
            /></View>
      <Button
        title="Sign Up"
        onPress={() => navigation.navigate('SignUp')}
      />
      <Button
        title="Forgot Password?"
        onPress={() => navigation.navigate('ForgotPassword')}
      />
    
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
 
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
    
    textAlign: 'center',
  },
  input: {
    marginBottom: 10,
    paddingHorizontal: 15,
    marginHorizontal:15,
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    borderRadius: 5,
  },
});

export default LoginScreen;
