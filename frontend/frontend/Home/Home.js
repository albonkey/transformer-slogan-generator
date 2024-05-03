import React, { useState } from 'react';
import { View, TextInput, ScrollView, KeyboardAvoidingView, Platform, TouchableWithoutFeedback, Keyboard, TouchableOpacity, Text, StyleSheet, Alert, Image } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';

const HomeScreen = ({ navigation }) => {
  const [companyName, setCompanyName] = useState('');
  const [description, setDescription] = useState('');

  const handleGenerateSlogan = () => {
    if (!companyName.trim() || !description.trim()) {
      Alert.alert("Missing Information", "Please fill in all fields.");
    } else {
      navigation.navigate('Loading', { companyName, description });
    }
  };

  return (
    <LinearGradient
      colors={['#d3d3d3', '#efefef']}
      start={{ x: 0, y: 0 }}
      end={{ x: 1, y: 0 }}
      style={styles.linearGradient}
    >
      <KeyboardAvoidingView
        style={styles.keyboardAvoidingView}
        behavior={Platform.OS === "ios" ? "padding" : "height"}
        keyboardVerticalOffset={Platform.OS === "ios" ? 64 : 0}
      >
        <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
          <ScrollView contentContainerStyle={styles.scrollView}>
            <View style={styles.logoContainer}>
              <Image
                source={require('../assets/logo.webp')}
                resizeMode='contain'
                style={styles.logo}
              />
            </View>
            <TextInput
              placeholder="Company Name"
              value={companyName}
              onChangeText={setCompanyName}
              style={styles.input}
            />
            <TextInput
              placeholder="Description"
              value={description}
              onChangeText={setDescription}
              style={styles.input}
            />
            <TouchableOpacity style={styles.button} onPress={handleGenerateSlogan}>
              <Text style={styles.buttonText}>Generate Slogan</Text>
            </TouchableOpacity>
          </ScrollView>
        </TouchableWithoutFeedback>
      </KeyboardAvoidingView>
    </LinearGradient>
  );
};

const styles = StyleSheet.create({
  linearGradient: {
    flex: 1,
  },
  keyboardAvoidingView: {
    flex: 1,
  },
  scrollView: {
    flexGrow: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingVertical: 20,
  },
  logoContainer: {
    marginVertical: 60,
  },
  logo: {
    height: 200,
    width: 300,
  },
  input: {
    width: '90%',
    marginVertical: 10,
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 15,
    borderRadius: 10,
    backgroundColor: 'white',
    elevation: 3,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 1.5,
  },
  button: {
    backgroundColor: '#007bff',
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 20,
    marginTop: 20,
    width: '90%',
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
    textAlign: 'center',
  },
});

export default HomeScreen;
