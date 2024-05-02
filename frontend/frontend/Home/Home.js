// HomeScreen.js
import React, { useState } from 'react';
import { View, TextInput, Button, StyleSheet, Alert } from 'react-native';

const HomeScreen = ({ navigation }) => {
  const [companyName, setCompanyName] = useState('');
  const [description, setDescription] = useState('');

  const handleGenerateSlogan = () => {
    // Debug output to verify state content


    // Check if the input fields are empty
    if (!companyName.trim() || !description.trim()) {
      // Alert if any field is empty
      Alert.alert("Missing Information", "Please fill in all fields.");
    }     
    else {
      
      // Navigate to LoadingScreen if all fields are filled
      // Debug: Check what is being sent to the next screen
      
      navigation.navigate('Loading',  {companyName, description} );
    }
  };

  return (
    <View style={styles.container}>
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
      <Button
        title="Generate Slogan"
        onPress={handleGenerateSlogan}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  input: {
    width: '100%',
    margin: 10,
    borderBottomWidth: 1,
    borderColor: 'gray',
    padding: 10,
  },
});

export default HomeScreen;
