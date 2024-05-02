import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import LoginScreen from './Home/Login';
import SignUpScreen from './Home/Signup'; 
import HomeScreen from './Home/Home';
import SloganDisplayScreen from './Home/Output'; 
import LoadingScreen from './Home/Loading';
//import ForgotPasswordScreen from './ForgotPasswordScreen'; // Assume this is another component you created

const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Login" 
        component={LoginScreen}
        options={{ headerShown: false }} />

        <Stack.Screen name="SignUp" 
        component={SignUpScreen}
        options={{ headerShown: false }} />

        <Stack.Screen name="Home" 
        component={HomeScreen}
        options={{ headerShown: false }} />

      <Stack.Screen name="Loading" 
        component={LoadingScreen}
        options={{ headerShown: false }} />

      <Stack.Screen name="Output" 
        component={SloganDisplayScreen}
        options={{ headerShown: false }} />
        
        
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
